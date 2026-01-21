# Permainan Kuis Sederhana
# Dibuat oleh GitHub Copilot

# Daftar pertanyaan dan jawaban
questions = [
    {
        "question": "Apa ibu kota Indonesia?",
        "answer": "Jakarta"
    },
    {
        "question": "Berapa hasil dari 2 + 2?",
        "answer": "4"
    },
    {
        "question": "Apa warna langit pada siang hari yang cerah?",
        "answer": "Biru"
    },
    {
        "question": "Siapa presiden pertama Indonesia?",
        "answer": "Soekarno"
    },
    {
        "question": "Apa nama planet terdekat dari Matahari?",
        "answer": "Merkurius"
    }
]

def main():
    print("Selamat datang di Permainan Kuis Sederhana!")
    print("Jawab pertanyaan berikut dengan benar.\n")

    score = 0
    total_questions = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"Pertanyaan {i}: {q['question']}")
        user_answer = input("Jawaban Anda: ").strip().lower()
        correct_answer = q['answer'].lower()

        if user_answer == correct_answer:
            print("Benar!\n")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah: {q['answer']}\n")

    print(f"Skor Anda: {score}/{total_questions}")
    if score == total_questions:
        print("Luar biasa! Anda menjawab semua dengan benar!")
    elif score >= total_questions // 2:
        print("Bagus! Anda cukup baik.")
    else:
        print("Coba lagi untuk meningkatkan skor Anda.")

if __name__ == "__main__":
    main()