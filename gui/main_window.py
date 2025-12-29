"""FastCopy v1.6 - Multi-language GUI"""
import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading, os, sys, time, string
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import RobocopyRunner, CopyOptions, CopyMode, ProgressInfo, CopyStatus
from utils import format_size, format_time, get_folder_size, get_disk_info, check_disk_space_warning, get_system_performance_info
from .languages import get_text, get_lang_code

ctk.set_default_color_theme("blue")
VER = "1.6"
DEF_THREADS, DEF_BUFFER = 8, 8
WARN_HI_T, WARN_LO_T, WARN_HI_B, WARN_LO_B = 24, 2, 64, 1


class FastCopyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.lang, self.dark = "vi", True
        ctk.set_appearance_mode("dark")
        self.title(f"⚡ FastCopy v{VER}")
        self.geometry("1050x900")
        self.minsize(1000, 850)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.runner = RobocopyRunner()
        self.start_time = self.total_size = self.total_files = self._log_idx = 0
        self.is_file_mode, self.source_files, self._job = False, [], None
        
        if not RobocopyRunner.is_available():
            messagebox.showerror("Error", "Robocopy not available!")
        self._build()
        
    def t(self, k, *a): return get_text(self.lang, k, *a)
    
    def _build(self):
        self._header()
        self._tabs()
        ctk.CTkLabel(self, text="Dev With ❤️ by Juong", font=ctk.CTkFont(size=11), text_color="gray").grid(row=2, column=0, pady=8)
        
    def _header(self):
        f = ctk.CTkFrame(self, fg_color="transparent")
        f.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="ew")
        f.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(f, text="⚡ FastCopy", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, sticky="w")
        self.sub = ctk.CTkLabel(f, text=self.t("subtitle"), font=ctk.CTkFont(size=10), text_color="gray")
        self.sub.grid(row=1, column=0, sticky="w")
        r = ctk.CTkFrame(f, fg_color="transparent")
        r.grid(row=0, column=1, rowspan=2, sticky="e")
        self.lang_m = ctk.CTkOptionMenu(r, values=["Tiếng Việt", "English", "日本語", "中文"], width=100, height=26, command=self._lang)
        self.lang_m.pack(side="left", padx=4)
        self.theme_b = ctk.CTkButton(r, text="☀️", width=30, height=26, fg_color="gray", command=self._theme)
        self.theme_b.pack(side="left", padx=4)
        ctk.CTkLabel(r, text=f"v{VER}", font=ctk.CTkFont(size=10), text_color="gray").pack(side="left", padx=6)
        
    def _tabs(self):
        self.tv = ctk.CTkTabview(self)
        self.tv.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")
        self.t_copy = self.tv.add(self.t("copy_tab"))
        self.t_disk = self.tv.add(self.t("disk_tab"))
        self.t_set = self.tv.add(self.t("settings_tab"))
        self.t_help = self.tv.add(self.t("help_tab"))
        self._tab_copy()
        self._tab_disk()
        self._tab_set()
        self._tab_help()
        
    def _tab_copy(self):
        t = self.t_copy
        t.grid_columnconfigure(0, weight=1)
        t.grid_rowconfigure(4, weight=1)
        # Paths
        pf = ctk.CTkFrame(t)
        pf.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        pf.grid_columnconfigure(1, weight=1)
        mf = ctk.CTkFrame(pf, fg_color="transparent")
        mf.grid(row=0, column=0, columnspan=3, padx=8, pady=(6,3), sticky="w")
        self.mode_v = ctk.StringVar(value="folder")
        self.r_fld = ctk.CTkRadioButton(mf, text=self.t("folder"), variable=self.mode_v, value="folder", command=self._mode_ch)
        self.r_fld.pack(side="left", padx=6)
        self.r_fil = ctk.CTkRadioButton(mf, text=self.t("files"), variable=self.mode_v, value="file", command=self._mode_ch)
        self.r_fil.pack(side="left", padx=6)
        self.l_src = ctk.CTkLabel(pf, text=self.t("source"), font=ctk.CTkFont(size=11, weight="bold"), width=50)
        self.l_src.grid(row=1, column=0, padx=8, pady=5, sticky="w")
        self.e_src = ctk.CTkEntry(pf, placeholder_text="...", height=34)
        self.e_src.grid(row=1, column=1, padx=4, pady=5, sticky="ew")
        self.b_src = ctk.CTkButton(pf, text=self.t("select"), width=55, height=34, command=self._br_src)
        self.b_src.grid(row=1, column=2, padx=8, pady=5)
        self.l_dst = ctk.CTkLabel(pf, text=self.t("dest"), font=ctk.CTkFont(size=11, weight="bold"), width=50)
        self.l_dst.grid(row=2, column=0, padx=8, pady=5, sticky="w")
        self.e_dst = ctk.CTkEntry(pf, placeholder_text="...", height=34)
        self.e_dst.grid(row=2, column=1, padx=4, pady=5, sticky="ew")
        self.b_dst = ctk.CTkButton(pf, text=self.t("select"), width=55, height=34, command=lambda: self._br_dir(self.e_dst))
        self.b_dst.grid(row=2, column=2, padx=8, pady=5)
        # Disk info
        df = ctk.CTkFrame(t)
        df.grid(row=1, column=0, padx=10, pady=3, sticky="ew")
        df.grid_columnconfigure((0,1), weight=1)
        self.l_sd = ctk.CTkLabel(df, text="💾 --", font=ctk.CTkFont(size=10), text_color="gray")
        self.l_sd.grid(row=0, column=0, padx=8, pady=3, sticky="w")
        self.l_dd = ctk.CTkLabel(df, text="💾 --", font=ctk.CTkFont(size=10), text_color="gray")
        self.l_dd.grid(row=0, column=1, padx=8, pady=3, sticky="w")
        self.l_warn = ctk.CTkLabel(df, text="", font=ctk.CTkFont(size=10), text_color="#FF6B6B")
        self.l_warn.grid(row=1, column=0, columnspan=2, padx=8, pady=2, sticky="w")
        # Options
        of = ctk.CTkFrame(t)
        of.grid(row=2, column=0, padx=10, pady=3, sticky="ew")
        r1 = ctk.CTkFrame(of, fg_color="transparent")
        r1.pack(fill="x", padx=8, pady=5)
        self.l_md = ctk.CTkLabel(r1, text=self.t("mode"), font=ctk.CTkFont(size=11))
        self.l_md.pack(side="left")
        self.cp_mode = ctk.StringVar(value="Copy")
        ctk.CTkOptionMenu(r1, values=["Copy", "Mirror", "Move"], variable=self.cp_mode, width=85, height=28).pack(side="left", padx=5)
        self.l_th = ctk.CTkLabel(r1, text=self.t("threads"), font=ctk.CTkFont(size=11))
        self.l_th.pack(side="left", padx=(12,3))
        self.v_th = ctk.IntVar(value=DEF_THREADS)
        ctk.CTkSlider(r1, from_=1, to=32, number_of_steps=31, variable=self.v_th, width=80, command=self._th_ch).pack(side="left")
        self.l_thv = ctk.CTkLabel(r1, text=str(DEF_THREADS), font=ctk.CTkFont(size=11, weight="bold"), width=22)
        self.l_thv.pack(side="left")
        self.l_bf = ctk.CTkLabel(r1, text=self.t("buffer"), font=ctk.CTkFont(size=11))
        self.l_bf.pack(side="left", padx=(12,3))
        self.e_bf = ctk.CTkEntry(r1, width=45, height=28)
        self.e_bf.pack(side="left")
        self.e_bf.insert(0, str(DEF_BUFFER))
        self.e_bf.bind("<FocusOut>", lambda e: self._chk_warn())
        self.v_bu = ctk.StringVar(value="MB")
        ctk.CTkOptionMenu(r1, values=["KB", "MB", "GB"], variable=self.v_bu, width=50, height=28).pack(side="left", padx=2)
        self.b_def = ctk.CTkButton(r1, text=self.t("default_btn"), width=80, height=28, fg_color="gray", command=self._reset)
        self.b_def.pack(side="left", padx=10)
        self.l_ow = ctk.CTkLabel(of, text="", font=ctk.CTkFont(size=10), text_color="#FFD93D")
        self.l_ow.pack(fill="x", padx=8, pady=2)
        r2 = ctk.CTkFrame(of, fg_color="transparent")
        r2.pack(fill="x", padx=8, pady=3)
        self.v_em, self.v_pa, self.v_re, self.v_at = ctk.BooleanVar(value=True), ctk.BooleanVar(value=True), ctk.BooleanVar(value=True), ctk.BooleanVar(value=True)
        self.c_em = ctk.CTkCheckBox(r2, text=self.t("empty_dirs"), variable=self.v_em)
        self.c_em.pack(side="left", padx=5)
        self.c_pa = ctk.CTkCheckBox(r2, text=self.t("parent_dir"), variable=self.v_pa)
        self.c_pa.pack(side="left", padx=5)
        self.c_re = ctk.CTkCheckBox(r2, text=self.t("retry"), variable=self.v_re)
        self.c_re.pack(side="left", padx=5)
        self.c_at = ctk.CTkCheckBox(r2, text=self.t("keep_attr"), variable=self.v_at)
        self.c_at.pack(side="left", padx=5)
        # Progress
        prf = ctk.CTkFrame(t)
        prf.grid(row=3, column=0, padx=10, pady=3, sticky="ew")
        h = ctk.CTkFrame(prf, fg_color="transparent")
        h.pack(fill="x", padx=8, pady=5)
        self.l_st = ctk.CTkLabel(h, text=self.t("ready"), font=ctk.CTkFont(size=12, weight="bold"))
        self.l_st.pack(side="left")
        self.l_eta = ctk.CTkLabel(h, text="", font=ctk.CTkFont(size=10), text_color="#FFD93D")
        self.l_eta.pack(side="left", padx=10)
        self.l_pct = ctk.CTkLabel(h, text="0%", font=ctk.CTkFont(size=18, weight="bold"), text_color="#00D4FF")
        self.l_pct.pack(side="right")
        self.l_el = ctk.CTkLabel(h, text="", font=ctk.CTkFont(size=10), text_color="#6BCB77")
        self.l_el.pack(side="right", padx=10)
        self.pbar = ctk.CTkProgressBar(prf, height=18, corner_radius=5)
        self.pbar.pack(fill="x", padx=8, pady=3)
        self.pbar.set(0)
        self.l_cf = ctk.CTkLabel(prf, text="", font=ctk.CTkFont(size=9), text_color="gray")
        self.l_cf.pack(fill="x", padx=8, pady=2)
        sf = ctk.CTkFrame(prf, fg_color="transparent")
        sf.pack(fill="x", padx=8, pady=5)
        self.l_fi = ctk.CTkLabel(sf, text="📄 0/0", font=ctk.CTkFont(size=10))
        self.l_fi.pack(side="left", padx=6)
        self.l_sz = ctk.CTkLabel(sf, text="💾 0 B", font=ctk.CTkFont(size=10))
        self.l_sz.pack(side="left", padx=6)
        self.l_tot = ctk.CTkLabel(sf, text="📦 0 B", font=ctk.CTkFont(size=10))
        self.l_tot.pack(side="left", padx=6)
        self.l_sp = ctk.CTkLabel(sf, text="🚀 --", font=ctk.CTkFont(size=10))
        self.l_sp.pack(side="left", padx=6)
        self.l_er = ctk.CTkLabel(sf, text="❌ 0", font=ctk.CTkFont(size=10))
        self.l_er.pack(side="left", padx=6)
        # Logs
        lf = ctk.CTkFrame(t)
        lf.grid(row=4, column=0, padx=10, pady=3, sticky="nsew")
        lf.grid_columnconfigure(0, weight=1)
        lf.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(lf, text="📋 Log", font=ctk.CTkFont(size=10, weight="bold")).grid(row=0, column=0, padx=8, pady=(5,2), sticky="w")
        self.log = ctk.CTkTextbox(lf, height=80, font=ctk.CTkFont(family="Consolas", size=9))
        self.log.grid(row=1, column=0, padx=8, pady=(0,6), sticky="nsew")
        # Buttons
        bf = ctk.CTkFrame(t, fg_color="transparent")
        bf.grid(row=5, column=0, padx=10, pady=8, sticky="ew")
        bf.grid_columnconfigure(1, weight=1)
        self.b_cl = ctk.CTkButton(bf, text=self.t("clear_log"), width=65, height=36, fg_color="gray", command=lambda: self.log.delete("1.0", "end"))
        self.b_cl.grid(row=0, column=0, padx=3)
        self.b_in = ctk.CTkButton(bf, text=self.t("info"), width=65, height=36, fg_color="#4A90D9", command=self._sysinfo)
        self.b_in.grid(row=0, column=1, padx=3, sticky="w")
        self.b_stop = ctk.CTkButton(bf, text=self.t("stop"), width=55, height=36, fg_color="#FF4444", command=self._stop, state="disabled")
        self.b_stop.grid(row=0, column=2, padx=3, sticky="e")
        self.b_start = ctk.CTkButton(bf, text=self.t("start"), width=100, height=36, font=ctk.CTkFont(size=12, weight="bold"), fg_color="#00AA55", command=self._start)
        self.b_start.grid(row=0, column=3, padx=3)
        
    def _tab_disk(self):
        t = self.t_disk
        t.grid_columnconfigure(0, weight=1)
        t.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(t, text=self.t("disk_info"), font=ctk.CTkFont(size=13, weight="bold")).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.dtf = ctk.CTkScrollableFrame(t, height=400)
        self.dtf.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.dtf.grid_columnconfigure(tuple(range(8)), weight=1)
        for i, h in enumerate([self.t("drive"), self.t("type"), self.t("model"), self.t("filesystem"), self.t("total"), self.t("used"), self.t("free"), self.t("percent")]):
            ctk.CTkLabel(self.dtf, text=h, font=ctk.CTkFont(size=10, weight="bold")).grid(row=0, column=i, padx=4, pady=4, sticky="w")
        self.drows = []
        self.b_ref = ctk.CTkButton(t, text=self.t("refresh"), width=100, height=34, command=self._ref_disk)
        self.b_ref.grid(row=2, column=0, padx=10, pady=10)
        self._ref_disk()
        
    def _ref_disk(self):
        for r in self.drows:
            for w in r: w.destroy()
        self.drows = []
        for l in string.ascii_uppercase:
            p = f"{l}:\\"
            if os.path.exists(p):
                d = get_disk_info(p)
                if d and d.total_bytes > 0:
                    ri = len(self.drows) + 1
                    pct = d.used_percent
                    c = "#6BCB77" if pct < 70 else ("#FFD93D" if pct < 90 else "#FF6B6B")
                    row = [
                        ctk.CTkLabel(self.dtf, text=f"{l}:\\", font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=d.drive_type, font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=(d.model[:25] if d.model else "-"), font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=d.file_system, font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=format_size(d.total_bytes), font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=format_size(d.used_bytes), font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=format_size(d.free_bytes), font=ctk.CTkFont(size=10)),
                        ctk.CTkLabel(self.dtf, text=f"{pct:.1f}%", font=ctk.CTkFont(size=10), text_color=c),
                    ]
                    for i, w in enumerate(row): w.grid(row=ri, column=i, padx=4, pady=3, sticky="w")
                    self.drows.append(row)
                    
    def _tab_set(self):
        t = self.t_set
        t.grid_columnconfigure(0, weight=1)
        thf = ctk.CTkFrame(t)
        thf.grid(row=0, column=0, padx=10, pady=8, sticky="ew")
        ctk.CTkLabel(thf, text=self.t("settings_title"), font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=10, pady=8)
        r1 = ctk.CTkFrame(thf, fg_color="transparent")
        r1.pack(fill="x", padx=10, pady=5)
        self.l_thm = ctk.CTkLabel(r1, text=self.t("theme"), font=ctk.CTkFont(size=11))
        self.l_thm.pack(side="left")
        self.m_thm = ctk.CTkOptionMenu(r1, values=[self.t("dark"), self.t("light")], width=120, height=28, command=self._thm_m)
        self.m_thm.pack(side="left", padx=8)
        syf = ctk.CTkFrame(t)
        syf.grid(row=1, column=0, padx=10, pady=8, sticky="ew")
        ctk.CTkLabel(syf, text=self.t("sys_info"), font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=10, pady=8)
        self.l_sys = ctk.CTkLabel(syf, text="...", font=ctk.CTkFont(size=10), text_color="gray", wraplength=800, justify="left")
        self.l_sys.pack(anchor="w", padx=10, pady=5)
        _, msg = get_system_performance_info()
        self.l_sys.configure(text=msg)
        opf = ctk.CTkFrame(t)
        opf.grid(row=2, column=0, padx=10, pady=8, sticky="ew")
        ctk.CTkLabel(opf, text=self.t("optimization"), font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=10, pady=8)
        tips = ctk.CTkTextbox(opf, height=150, font=ctk.CTkFont(size=10))
        tips.pack(fill="x", padx=10, pady=5)
        tips.insert("1.0", self.t("opt_tips"))
        tips.configure(state="disabled")
        
    def _tab_help(self):
        t = self.t_help
        t.grid_columnconfigure(0, weight=1)
        hf = ctk.CTkFrame(t)
        hf.grid(row=0, column=0, padx=10, pady=8, sticky="ew")
        ctk.CTkLabel(hf, text=self.t("help_title"), font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=10, pady=8)
        ht = ctk.CTkTextbox(hf, height=200, font=ctk.CTkFont(size=11))
        ht.pack(fill="x", padx=10, pady=5)
        ht.insert("1.0", self.t("help_content"))
        ht.configure(state="disabled")
        tf = ctk.CTkFrame(t)
        tf.grid(row=1, column=0, padx=10, pady=8, sticky="ew")
        ctk.CTkLabel(tf, text=self.t("terms_title"), font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=10, pady=8)
        tt = ctk.CTkTextbox(tf, height=150, font=ctk.CTkFont(size=11))
        tt.pack(fill="x", padx=10, pady=5)
        tt.insert("1.0", self.t("terms_content"))
        tt.configure(state="disabled")
        
    # Handlers
    def _lang(self, s):
        self.lang = get_lang_code(s)
        self._upd_txt()
        
    def _upd_txt(self):
        self.sub.configure(text=self.t("subtitle"))
        self.l_st.configure(text=self.t("ready"))
        self.b_src.configure(text=self.t("select"))
        self.b_dst.configure(text=self.t("select"))
        self.b_start.configure(text=self.t("start"))
        self.b_stop.configure(text=self.t("stop"))
        self.b_cl.configure(text=self.t("clear_log"))
        self.b_in.configure(text=self.t("info"))
        self.b_def.configure(text=self.t("default_btn"))
        self.b_ref.configure(text=self.t("refresh"))
        self.l_src.configure(text=self.t("source"))
        self.l_dst.configure(text=self.t("dest"))
        self.l_md.configure(text=self.t("mode"))
        self.l_th.configure(text=self.t("threads"))
        self.l_bf.configure(text=self.t("buffer"))
        self.l_thm.configure(text=self.t("theme"))
        self.c_em.configure(text=self.t("empty_dirs"))
        self.c_pa.configure(text=self.t("parent_dir"))
        self.c_re.configure(text=self.t("retry"))
        self.c_at.configure(text=self.t("keep_attr"))
        self.r_fld.configure(text=self.t("folder"))
        self.r_fil.configure(text=self.t("files"))
        
    def _theme(self):
        self.dark = not self.dark
        ctk.set_appearance_mode("dark" if self.dark else "light")
        self.theme_b.configure(text="☀️" if self.dark else "🌙")
        self.m_thm.set(self.t("dark") if self.dark else self.t("light"))
        
    def _thm_m(self, s):
        is_d = self.t("dark") in s
        if is_d != self.dark: self._theme()
        
    def _reset(self):
        self.v_th.set(DEF_THREADS)
        self.l_thv.configure(text=str(DEF_THREADS))
        self.e_bf.delete(0, "end")
        self.e_bf.insert(0, str(DEF_BUFFER))
        self.v_bu.set("MB")
        self.l_ow.configure(text="")
        
    def _th_ch(self, v):
        self.l_thv.configure(text=str(int(v)))
        self._chk_warn()
        
    def _chk_warn(self):
        w = []
        th = self.v_th.get()
        if th > WARN_HI_T: w.append(self.t("warn_high_threads", WARN_HI_T))
        elif th < WARN_LO_T: w.append(self.t("warn_low_threads", WARN_LO_T))
        try:
            bf = int(self.e_bf.get())
            u = self.v_bu.get()
            bm = bf * (1 if u == "MB" else (0.001 if u == "KB" else 1024))
            if bm > WARN_HI_B: w.append(self.t("warn_high_buffer", WARN_HI_B))
            elif bm < WARN_LO_B: w.append(self.t("warn_low_buffer", WARN_LO_B))
        except: pass
        self.l_ow.configure(text=" | ".join(w))
        
    def _mode_ch(self):
        self.is_file_mode = self.mode_v.get() == "file"
        self.e_src.delete(0, "end")
        self.source_files = []
        
    def _br_src(self):
        if self.is_file_mode:
            fs = filedialog.askopenfilenames(title=self.t("select"))
            if fs:
                self.source_files = list(fs)
                self.e_src.delete(0, "end")
                self.e_src.insert(0, fs[0] if len(fs) == 1 else f"[{len(fs)} files]")
                self._upd_info()
        else: self._br_dir(self.e_src, True)
        
    def _br_dir(self, e, is_src=False):
        d = filedialog.askdirectory()
        if d:
            e.delete(0, "end")
            e.insert(0, d)
            self._upd_info()
            
    def _upd_info(self):
        src, dst = self.e_src.get().strip(), self.e_dst.get().strip()
        if self.is_file_mode and self.source_files:
            self.total_size = sum(os.path.getsize(f) for f in self.source_files if os.path.exists(f))
            self.total_files = len(self.source_files)
            d = get_disk_info(self.source_files[0]) if self.source_files else None
            if d: self.l_sd.configure(text=f"💾 {d.drive_letter}: {d.model or d.label} | {d.drive_type}")
        elif src and os.path.exists(src):
            self.total_size, self.total_files = get_folder_size(src)
            d = get_disk_info(src)
            if d: self.l_sd.configure(text=f"💾 {d.drive_letter}: {d.model or d.label} | {d.drive_type} | {format_size(d.total_bytes)}")
        else: self.l_sd.configure(text="💾 --")
        self.l_tot.configure(text=f"📦 {format_size(self.total_size)}")
        if dst:
            p = dst if os.path.exists(dst) else os.path.dirname(dst)
            if p and os.path.exists(p):
                d = get_disk_info(p)
                if d:
                    c = "#6BCB77" if d.free_percent > 20 else ("#FFD93D" if d.free_percent > 10 else "#FF6B6B")
                    self.l_dd.configure(text=f"💾 {d.drive_letter}: {d.model or d.label} | {d.drive_type} | {format_size(d.free_bytes)}", text_color=c)
                    if self.total_size > 0:
                        w, m = check_disk_space_warning(self.total_size, p)
                        self.l_warn.configure(text=f"⚠️ {m}" if w else "")
        else:
            self.l_dd.configure(text="💾 --", text_color="gray")
            self.l_warn.configure(text="")
            
    def _log(self, m):
        self.log.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] {m}\n")
        self.log.see("end")
        
    def _sysinfo(self):
        _, m = get_system_performance_info()
        messagebox.showinfo(self.t("info_title"), m)
        
    def _upd_ui(self, p: ProgressInfo):
        st = {CopyStatus.PENDING: self.t("ready"), CopyStatus.RUNNING: self.t("copying"), CopyStatus.COMPLETED: self.t("done"), CopyStatus.FAILED: self.t("error"), CopyStatus.CANCELLED: self.t("stopped")}
        self.l_st.configure(text=st.get(p.status, ""))
        pct = 0
        if self.total_size > 0 and p.bytes_copied > 0: pct = min((p.bytes_copied / self.total_size) * 100, 100)
        elif p.percent > 0: pct = p.percent
        elif self.total_files > 0 and p.files_copied > 0: pct = (p.files_copied / self.total_files) * 100
        self.pbar.set(pct / 100)
        self.l_pct.configure(text=f"{pct:.1f}%")
        if self.start_time:
            el = time.time() - self.start_time
            self.l_el.configure(text=f"⏱️ {format_time(el)}")
            if 0 < pct < 100:
                rem = (el / pct) * (100 - pct)
                self.l_eta.configure(text=f"⏳ ~{format_time(rem)}")
            elif pct >= 100: self.l_eta.configure(text="✅")
        if p.current_file:
            cf = p.current_file
            self.l_cf.configure(text=f"📄 {cf[-65:] if len(cf) > 65 else cf}")
        ft = p.files_total or self.total_files
        self.l_fi.configure(text=f"📄 {p.files_copied}/{ft}")
        self.l_sz.configure(text=f"💾 {format_size(p.bytes_copied)}")
        if self.start_time:
            el = time.time() - self.start_time
            if el > 0 and p.bytes_copied > 0: self.l_sp.configure(text=f"🚀 {p.bytes_copied/el/1024/1024:.1f} MB/s")
        self.l_er.configure(text=f"❌ {len(p.errors)}")
        new = p.log_lines[self._log_idx:]
        for ln in new[-5:]: self.log.insert("end", f"{ln}\n")
        self.log.see("end")
        self._log_idx = len(p.log_lines)
        if p.status in [CopyStatus.COMPLETED, CopyStatus.FAILED, CopyStatus.CANCELLED]:
            self.b_start.configure(state="normal")
            self.b_stop.configure(state="disabled")
            if self._job: self.after_cancel(self._job); self._job = None
            if self.start_time: self._log(self.t("done_in", format_time(time.time() - self.start_time)))
            
    def _cb(self, p: ProgressInfo): self.after(0, lambda: self._upd_ui(p))
    def _timer(self):
        if self.runner.is_running() and self.start_time:
            self.l_el.configure(text=f"⏱️ {format_time(time.time() - self.start_time)}")
            self._job = self.after(500, self._timer)
            
    def _cp_th(self, src, dst, opts):
        try:
            self.runner.set_totals(self.total_size, self.total_files)
            for _ in self.runner.copy(src, dst, opts, self._cb): pass
        except Exception as e:
            self.after(0, lambda: self._log(self.t("log_error", e)))
            self.after(0, lambda: self.b_start.configure(state="normal"))
            self.after(0, lambda: self.b_stop.configure(state="disabled"))
            
    def _start(self):
        dst = self.e_dst.get().strip()
        if self.is_file_mode:
            if not self.source_files: return messagebox.showerror(self.t("error_title"), self.t("error_no_source"))
            src, files = os.path.dirname(self.source_files[0]), [os.path.basename(f) for f in self.source_files]
        else:
            src, files = self.e_src.get().strip(), []
        if not src: return messagebox.showerror(self.t("error_title"), self.t("error_no_source"))
        if not dst: return messagebox.showerror(self.t("error_title"), self.t("error_no_dest"))
        if not self.is_file_mode and not os.path.exists(src): return messagebox.showerror(self.t("error_title"), self.t("error_source_not_found"))
        actual = os.path.join(dst, os.path.basename(src)) if not self.is_file_mode and self.v_pa.get() else dst
        modes = {"Copy": CopyMode.COPY, "Mirror": CopyMode.MIRROR, "Move": CopyMode.MOVE}
        opts = CopyOptions(mode=modes.get(self.cp_mode.get(), CopyMode.COPY), threads=self.v_th.get(), copy_empty_dirs=self.v_em.get(), copy_subdirs=not self.is_file_mode, retry_count=3 if self.v_re.get() else 0, copy_attributes=self.v_at.get(), copy_timestamps=self.v_at.get(), include_patterns=files)
        self._log(self.t("log_start", src, actual))
        self._log(self.t("log_info", opts.threads, format_size(self.total_size), self.total_files))
        self.start_time, self._log_idx = time.time(), 0
        self.pbar.set(0); self.l_pct.configure(text="0%"); self.l_cf.configure(text=self.t("preparing")); self.l_fi.configure(text=f"📄 0/{self.total_files}"); self.l_sz.configure(text="💾 0 B"); self.l_sp.configure(text="🚀 --"); self.l_er.configure(text="❌ 0"); self.l_eta.configure(text="⏳"); self.l_el.configure(text="⏱️ 0s")
        self.b_start.configure(state="disabled"); self.b_stop.configure(state="normal")
        threading.Thread(target=self._cp_th, args=(src, actual, opts), daemon=True).start()
        self._timer()
        
    def _stop(self):
        if messagebox.askyesno(self.t("confirm_stop_title"), self.t("confirm_stop")):
            self.runner.cancel()
            self._log(self.t("log_stopping"))


def main(): FastCopyApp().mainloop()
if __name__ == "__main__": main()
