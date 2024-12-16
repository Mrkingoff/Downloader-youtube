import os
import time
import webbrowser
from termcolor import colored
from pytube import Search, YouTube
from yt_dlp import YoutubeDL

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan logo dan menu utama
def display_menu():
    logo = colored("""
╔════╦══╦╗╔═╦═══╦══╗
╚══╗═╠╣╠╣║║╔╣╔═╗╠╣╠╝
──╔╝╔╝║║║╚╝╝║╚═╝║║║─
─╔╝╔╝─║║║╔╗║║╔╗╔╝║║─
╔╝═╚═╦╣╠╣║║╚╣║║╚╦╣╠╗
╚════╩══╩╝╚═╩╝╚═╩══╝
""", "green")
    print(logo)
    print(colored("Creator : ©Zikri", "green"))
    print(colored("Telegram : t.me/zikriu", "red"))
    print(colored("WhatsApp : +6283853240293", "yellow"))
    print("\n1. PutarAudio <text>")
    print("2. YTMP3 (Link video YouTube)")
    print("3. YTMP4 (Link video YouTube)")
    print("4. Kata-kata Keren")
    print("5. Animasi Kereta Api")
    print("6. Hack Sosial (Fitur tidak tersedia)")
    print("7. Buat Link Sosial")
    print("0. Keluar")
    print()

# Fungsi untuk menampilkan kata-kata keren
def display_kata_kata():
    clear_screen()
    kata_kata = [
        "Hidup itu seperti bersepeda, agar tetap seimbang, kamu harus terus bergerak.",
        "Jangan menunggu kesempatan datang, ciptakan kesempatanmu sendiri.",
        "Kesuksesan tidak datang begitu saja, tetapi lewat kerja keras dan ketekunan.",
        "Kegagalan bukan akhir dari segalanya, tetapi langkah menuju kesuksesan.",
        "Berkarya adalah cara terbaik untuk menunjukkan siapa diri kita.",
        "Jangan takut untuk mencoba hal baru, karena disitulah letak peluang.",
        "Jangan pernah menyerah, karena kamu tidak tahu seberapa dekat kamu dengan kesuksesan.",
        "Ketika kamu berhenti belajar, kamu berhenti tumbuh.",
        "Keberhasilan adalah hasil dari keputusan yang tepat dan waktu yang tepat.",
        "Sukses tidak datang dari apa yang kamu lakukan sesekali, tetapi dari apa yang kamu lakukan setiap hari.",
        "Jadilah perubahan yang ingin kamu lihat di dunia.",
        "Hidupmu adalah cerminan dari apa yang kamu pikirkan."
    ]
    print(colored("12 Kata-kata Keren:\n", "green"))
    for i, kata in enumerate(kata_kata, 1):
        print(colored(f"{i}. {kata}", "green"))
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi untuk membuat animasi kereta api dengan efek warna
def animasi_kereta_api():
    clear_screen()
    kereta = [
        "  _______         _____",
        " |       |       |     |",
        " |_______|       |     |",
        "   o   o          o   o"
    ]
    
    colors = ['green', 'yellow', 'red', 'cyan', 'magenta']
    while True:
        for color in colors:
            clear_screen()
            for line in kereta:
                print(colored(line, color))
            time.sleep(0.3)  # Delay untuk memberi efek animasi
            clear_screen()

        # Stop animasi dengan menekan tombol 'q'
        stop = input("Tekan 'q' untuk berhenti atau Enter untuk melanjutkan animasi: ")
        if stop.lower() == 'q':
            break

# Fungsi untuk mengunduh audio dari YouTube
def download_audio(search_query):
    clear_screen()
    print(colored(f"Mencari lagu: {search_query}...", "green"))
    search = Search(search_query)
    result = search.results
    if result:
        video = result[0]  # Ambil hasil pertama
        print(colored(f"Mengunduh audio: {video.title}", "green"))
        yt = YouTube(video.watch_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = "downloads"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        audio_stream.download(output_path)
        print(colored(f"Audio berhasil diunduh ke folder '{output_path}'", "green"))
    else:
        print(colored("Tidak ada hasil ditemukan.", "red"))
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi untuk mengunduh MP3 dari link YouTube
def download_ytmp3(link):
    clear_screen()
    print(colored(f"Mengunduh MP3 dari: {link}", "green"))
    output_path = "downloads"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
    }
    with YoutubeDL(options) as ydl:
        ydl.download([link])
    print(colored(f"MP3 berhasil diunduh ke folder '{output_path}'", "green"))
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi untuk mengunduh MP4 dari link YouTube
def download_ytmp4(link):
    clear_screen()
    print(colored(f"Mengunduh MP4 dari: {link}", "green"))
    output_path = "downloads"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
    }
    with YoutubeDL(options) as ydl:
        ydl.download([link])
    print(colored(f"Video berhasil diunduh ke folder '{output_path}'", "green"))
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi untuk membuka Telegram
def open_telegram():
    clear_screen()
    print(colored("Membuka Telegram...", "green"))
    webbrowser.open("https://t.me/zikriu")
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi untuk membuat link sosial
def create_social_links():
    clear_screen()
    name = input(colored("Masukkan nama atau username sosial media: ", "yellow"))
    print(colored(f"Link untuk TikTok: https://www.tiktok.com/@{name}", "green"))
    print(colored(f"Link untuk Facebook: https://www.facebook.com/{name}", "green"))
    print(colored(f"Link untuk Telegram: https://t.me/{name}", "green"))
    print(colored(f"Link untuk Instagram: https://www.instagram.com/{name}", "green"))
    input("Tekan Enter untuk kembali ke menu utama...")

# Fungsi utama untuk menjalankan aplikasi
def main():
    while True:
        display_menu()
        try:
            choice = int(input(colored("Pilih menu: ", "yellow")))
            print()
            if choice == 1:
                search_query = input(colored("Masukkan judul lagu: ", "yellow"))
                download_audio(search_query)
            elif choice == 2:
                link = input(colored("Masukkan link video YouTube: ", "yellow"))
                download_ytmp3(link)
            elif choice == 3:
                link = input(colored("Masukkan link video YouTube: ", "yellow"))
                download_ytmp4(link)
            elif choice == 4:
                display_kata_kata()
            elif choice == 5:
                animasi_kereta_api()
            elif choice == 6:
                print(colored("Fitur hack sosial tidak tersedia.", "red"))
                input("Tekan Enter untuk kembali ke menu utama...")
            elif choice == 7:
                create_social_links()
            elif choice == 0:
                print(colored("Keluar dari program. Terima kasih!", "green"))
                break
            else:
                print(colored("Pilihan tidak valid. Coba lagi.", "red"))
        except ValueError:
            print(colored("Input tidak valid. Masukkan angka sesuai menu.", "red"))

if __name__ == "__main__":
    main()
