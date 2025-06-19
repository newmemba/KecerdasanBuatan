import tkinter as tk
from tkinter import ttk, messagebox

class AplikasiPrediksiPsikologi:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Prediksi Risiko Psikologi Mahasiswa")
        self.root.geometry("800x600")
        
        self.daftar_gejala = [
            "Insomnia (sulit tidur)",
            "Kelelahan berlebihan",
            "Serangan cemas/panik",
            "Menghindari situasi sosial",
            "Perasaan sedih berkepanjangan",
            "Kehilangan minat pada aktivitas",
            "Perubahan nafsu makan (naik/turun)",
            "Sulit berkonsentrasi",
            "Perasaan tidak berharga",
            "Pikiran tentang kematian",
            "Sakit kepala tanpa sebab medis",
            "Nyeri otot tanpa sebab jelas",
            "Perubahan berat badan signifikan",
            "Mudah marah/tersinggung",
            "Perasaan putus asa",
            "Konsumsi alkohol berlebihan",
            "Mengisolasi diri",
            "Menurunnya prestasi akademik",
            "Kesulitan membuat keputusan",
            "Perasaan bersalah berlebihan"
        ]
        
        self.gejala_terpilih = []
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Sistem Prediksi Risiko Psikologi Mahasiswa", 
                 font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, 
                 text="Pilih gejala yang Anda alami dalam 2 minggu terakhir:",
                 font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W)
        
 
        gejala_frame = ttk.Frame(main_frame)
        gejala_frame.grid(row=2, column=0, sticky=tk.NSEW, pady=10)
        
        scrollbar = ttk.Scrollbar(gejala_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox_gejala = tk.Listbox(gejala_frame, selectmode=tk.MULTIPLE, 
                                       yscrollcommand=scrollbar.set,
                                       height=15, width=60, font=("Helvetica", 11))
        self.listbox_gejala.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox_gejala.yview)
        
        for gejala in self.daftar_gejala:
            self.listbox_gejala.insert(tk.END, gejala)
        
     
        ttk.Button(main_frame, text="Prediksi Risiko", 
                  command=self.lakukan_prediksi).grid(row=3, column=0, pady=20)
        
 
        self.hasil_frame = ttk.LabelFrame(main_frame, text="Hasil Prediksi", padding=10)
        self.hasil_frame.grid(row=4, column=0, sticky=tk.EW, pady=10)
        
      
        self.label_hasil = ttk.Label(self.hasil_frame, text="Silakan pilih gejala terlebih dahulu",
                                   font=("Helvetica", 12), wraplength=500)
        self.label_hasil.pack()
        
        
        self.label_rekomendasi = ttk.Label(self.hasil_frame, text="", 
                                         font=("Helvetica", 11, "italic"), wraplength=500)
        self.label_rekomendasi.pack(pady=10)
        
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
    
    def lakukan_prediksi(self):
        selected_indices = self.listbox_gejala.curselection()
        self.gejala_terpilih = [self.daftar_gejala[i] for i in selected_indices]
        
        if not self.gejala_terpilih:
            messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala")
            return
        
  
        gejala_sistem = set()
        for gejala in self.gejala_terpilih:
            if "Insomnia" in gejala:
                gejala_sistem.add("insomnia")
            elif "Kelelahan" in gejala:
                gejala_sistem.add("kelelahan")
            elif "cemas/panik" in gejala:
                gejala_sistem.add("serangan_cemas")
            elif "sosial" in gejala:
                gejala_sistem.add("menghindar")
            elif "sedih" in gejala:
                gejala_sistem.add("sedih")
            elif "minat" in gejala:
                gejala_sistem.add("kehilangan_minat")
            elif "nafsu makan" in gejala:
                gejala_sistem.add("perubahan_nafsu_makan")
            elif "konsentrasi" in gejala:
                gejala_sistem.add("sulit_konsentrasi")
            elif "berharga" in gejala:
                gejala_sistem.add("tidak_berharga")
            elif "kematian" in gejala:
                gejala_sistem.add("pikiran_kematian")
        
 
        risiko = self.prediksi_risiko(gejala_sistem)
        
    
        self.tampilkan_hasil(risiko)
    
    def prediksi_risiko(self, gejala):
        
        aturan = [
            {
                "kondisi": {"insomnia", "kelelahan", "sulit_konsentrasi"},
                "kesimpulan": "risiko_stres_akademik",
                "deskripsi": "Stres Akademik Tinggi",
                "rekomendasi": "Istirahat cukup, atur jadwal belajar, bicarakan dengan dosen atau teman"
            },
            {
                "kondisi": {"serangan_cemas", "menghindar", "kelelahan"},
                "kesimpulan": "risiko_gangguan_kecemasan",
                "deskripsi": "Gangguan Kecemasan",
                "rekomendasi": "Latihan pernapasan, kurangi kafein, pertimbangkan konsultasi psikolog"
            },
            {
                "kondisi": {"sedih", "kehilangan_minat", "perubahan_nafsu_makan", "tidak_berharga"},
                "kesimpulan": "risiko_depresi",
                "deskripsi": "Depresi Ringan-Sedang",
                "rekomendasi": "Cari dukungan sosial, pertahankan rutinitas sehat, pertimbangkan konseling"
            },
            {
                "kondisi": {"pikiran_kematian", "tidak_berharga", "sedih"},
                "kesimpulan": "risiko_depresi_berat",
                "deskripsi": "Depresi Berat (Segera cari bantuan profesional)",
                "rekomendasi": "Segera hubungi psikolog/psikiater atau layanan darurat kesehatan mental"
            },
            {
                "kondisi": {"risiko_stres_akademik", "risiko_gangguan_kecemasan"},
                "kesimpulan": "risiko_burnout",
                "deskripsi": "Risiko Burnout Akademik",
                "rekomendasi": "Evaluasi beban studi, ambil cuti jika perlu, cari dukungan kampus"
            }
        ]
        
        
        fakta = gejala.copy()
        perubahan = True
        hasil_prediksi = []
        while perubahan:
            perubahan = False
            for rule in aturan:
                if rule["kondisi"].issubset(fakta) and rule["kesimpulan"] not in fakta:
                    fakta.add(rule["kesimpulan"])
                    hasil_prediksi.append({
                        "jenis": rule["deskripsi"],
                        "rekomendasi": rule["rekomendasi"]})
                    perubahan = True
        if not hasil_prediksi:
            hasil_prediksi.append({
                "jenis": "Tidak terdeteksi risiko psikologis spesifik",
                "rekomendasi": "Tetap jaga kesehatan mental dengan pola hidup seimbang"
            })
        return hasil_prediksi
    
    def tampilkan_hasil(self, risiko):
      
        teks_hasil = "Gejala yang dipilih:\n"
        teks_hasil += "\n".join(f"- {g}" for g in self.gejala_terpilih)
        teks_hasil += "\n\nHasil Prediksi:\n"
        
        for r in risiko:
            teks_hasil += f"\n• {r['jenis']}"
        self.label_hasil.config(text=teks_hasil)
        if len(risiko) > 0:
            rekomendasi = "\nRekomendasi:\n" + risiko[0]['rekomendasi']
            if "berat" in risiko[0]['jenis'].lower():
                rekomendasi =  rekomendasi.upper()
            self.label_rekomendasi.config(text=rekomendasi)
        else:
            self.label_rekomendasi.config(text="")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPrediksiPsikologi(root)
    root.mainloop()