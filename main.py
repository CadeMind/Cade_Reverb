import json
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


def calculate_delays(bpm: int) -> dict:
    """Return common delay times in milliseconds for given BPM."""
    if bpm <= 0:
        raise ValueError("BPM must be positive")
    quarter_ms = 60000 / bpm
    delays = {
        "1/4": quarter_ms,
        "1/8": quarter_ms / 2,
        "1/16": quarter_ms / 4,
        "1/4 dot": quarter_ms * 1.5,
        "1/8 triplet": quarter_ms / 3,
    }
    return {k: round(v, 2) for k, v in delays.items()}


def load_presets() -> dict:
    """Load genre presets from JSON file."""
    presets_path = Path(__file__).with_name("genre_presets.json")
    if presets_path.exists():
        with presets_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class ReverbApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CADE: Reverb Timing Calculator")
        self.resizable(False, False)
        self.presets = load_presets()
        self.create_widgets()

    def create_widgets(self):
        # BPM input
        bpm_frame = ttk.Frame(self)
        bpm_frame.pack(padx=10, pady=5, fill="x")

        ttk.Label(bpm_frame, text="BPM:").pack(side="left")
        self.bpm_var = tk.StringVar(value="120")
        self.bpm_entry = ttk.Entry(bpm_frame, textvariable=self.bpm_var, width=7)
        self.bpm_entry.pack(side="left")
        self.bpm_entry.bind("<Return>", lambda _e: self.calculate())

        # Genre dropdown
        genre_frame = ttk.Frame(self)
        genre_frame.pack(padx=10, pady=5, fill="x")

        ttk.Label(genre_frame, text="Genre:").pack(side="left")
        genres = sorted(self.presets.keys()) if self.presets else ["-"]
        self.genre_var = tk.StringVar(value=genres[0])
        self.genre_combo = ttk.Combobox(genre_frame, textvariable=self.genre_var, values=genres, state="readonly")
        self.genre_combo.pack(side="left")

        # Calculate button
        calc_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calc_btn.pack(pady=5)

        # Delay table
        self.table = ttk.Treeview(self, columns=("note", "ms"), show="headings", height=5)
        self.table.heading("note", text="Note")
        self.table.heading("ms", text="Time (ms)")
        self.table.column("note", width=80, anchor="center")
        self.table.column("ms", width=100, anchor="center")
        self.table.pack(padx=10, pady=5)

        # Preset info
        info_frame = ttk.LabelFrame(self, text="Preset")
        info_frame.pack(fill="x", padx=10, pady=5)
        self.pre_delay_var = tk.StringVar()
        self.decay_var = tk.StringVar()
        self.type_var = tk.StringVar()
        ttk.Label(info_frame, text="Pre-delay:").grid(row=0, column=0, sticky="w")
        ttk.Label(info_frame, textvariable=self.pre_delay_var).grid(row=0, column=1, sticky="w")
        ttk.Label(info_frame, text="Decay:").grid(row=1, column=0, sticky="w")
        ttk.Label(info_frame, textvariable=self.decay_var).grid(row=1, column=1, sticky="w")
        ttk.Label(info_frame, text="Type:").grid(row=2, column=0, sticky="w")
        ttk.Label(info_frame, textvariable=self.type_var).grid(row=2, column=1, sticky="w")

        # Tips
        ttk.Label(self, text="Tips:").pack(anchor="w", padx=10)
        self.tips_text = tk.Text(self, height=4, width=40, wrap="word")
        self.tips_text.pack(padx=10, pady=5)
        self.tips_text.config(state="disabled")

    def calculate(self):
        try:
            bpm = int(self.bpm_var.get())
            if not 60 <= bpm <= 180:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid BPM", "Enter BPM between 60 and 180")
            return

        delays = calculate_delays(bpm)
        self.table.delete(*self.table.get_children())
        for note, ms in delays.items():
            self.table.insert("", "end", values=(note, ms))

        genre = self.genre_var.get()
        info = self.find_preset(genre, bpm)
        self.pre_delay_var.set(info.get("pre_delay", "-"))
        self.decay_var.set(info.get("decay", "-"))
        self.type_var.set(info.get("type", "-"))
        tips = "\n".join(info.get("tips", []))
        self.tips_text.config(state="normal")
        self.tips_text.delete("1.0", "end")
        self.tips_text.insert("end", tips)
        self.tips_text.config(state="disabled")

    def find_preset(self, genre: str, bpm: int) -> dict:
        genre_data = self.presets.get(genre, {})
        ranges = genre_data.get("bpm_ranges", {})
        for range_str, values in ranges.items():
            low, high = map(int, range_str.split("-"))
            if low <= bpm <= high:
                return values
        return {}


if __name__ == "__main__":
    app = ReverbApp()
    app.mainloop()
