# TodoApp
A simple yet powerful To-Do List application built with Python and Tkinter. This app helps you organize your tasks, stay productive, and even keeps you motivated with dynamic motivational messages.


## 🚀 Features

* ✅ Add, Edit, and Delete tasks easily
* 💾 **Persistent storage** (tasks are saved in `tasks.txt` automatically)
* 🎨 Clean and simple **GUI with Tkinter**
* 🖥️ Can be converted into a **standalone .exe application** (using PyInstaller)

## 🛠️ Tech Stack

* **Language**: Python
* **GUI Framework**: Tkinter
* **File Handling**: Plain text (`tasks.txt`)
* **Packaging**: PyInstaller (for .exe build)


## 📂 Project Structure

```
TodoApp/
│── todo_gui.py   # Main application file
│── tasks.txt     # Auto-created file to store tasks
```

---

## ▶️ How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/TodoApp.git
   cd TodoApp
   ```
2. Run the app:

   ```bash
   python todo_gui.py
   ```
3. (Optional) Build an `.exe`:

   ```bash
   pyinstaller --onefile --windowed todo_gui.py
   ```


## 🌱 Future Improvements

* Add **due dates & deadlines**
* Add **categories (Work, Study, Personal)**
* Sync tasks with a **database or cloud storage**
* Add **search/filter option**
* Export tasks to `.csv` or `.pdf`

---

## ✨ Author

👩‍💻 Developed by **\Haritha_Jana** – Passionate about Python & building simple apps that make life easier.

