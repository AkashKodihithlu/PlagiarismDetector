# CodeGuard

CodeGuard is a sophisticated multi-language code plagiarism detection system designed to analyze and identify structural and textual similarities across algorithm implementations. Using a multi-pipeline detection engine, CodeGuard can analyze Python, Java, C, and C++ source code to accurately detect algorithm types and measure code similarity against a vast dataset.

## Features

* **Multi-Language Support**: Analyzes code implementations written in Python, Java, C, and C++.
* **Advanced Detection Engine**: Combines multiple layers of similarity matching to prevent false positives and catch sophisticated obfuscation. 
* **Algorithm Detection**: Automatically identifies common algorithms (e.g., Bubble Sort, Quick Sort, Merge Sort) to restrict comparison scopes and dramatically improve processing speed.
* **Scan History Dashboard**: Review past plagiarism scans and detailed similarity scores.
* **Granular Results**: Provides percentage breakdowns for TF-IDF, AST, and Winnowing strategies, along with copied line highlights.
* **Secure Authentication**: JWT-based login and signup system with robust password validation constraints.

## Technology Stack

**Backend**
* **Framework:** FastAPI
* **Language:** Python
* **Database:** MongoDB
* **Engine/Algorithm Modules:** Scikit-Learn (TF-IDF), Python `ast` module, Custom Winnowing Hash algorithms.

**Frontend**
* **Framework:** React + Vite
* **Styling:** TailwindCSS + Custom Glassmorphism UI Components

## Detection Algorithms

CodeGuard employs a weighted multi-algorithmic pipeline based on the uploaded file's language to produce a highly accurate `final_score`:

1.  **TF-IDF Similarity**: Analyzes character-level n-grams and calculates document cosine similarity to catch direct copy-pasting and minor textual substitutions.
2.  **Winnowing Fingerprint Algorithm**: Uses sliding window hashing and Jaccard similarity to identify structural similarities irrespective of variable renaming, formatting, or whitespace changes.
3.  **AST Structural Similarity (Python Only)**: Extracts and compares Abstract Syntax Tree tokens to detect structural plagiarism even if the textual code looks vastly different.

*(Detection weights dynamically shift. For example, Python uses a blend of TF-IDF, AST, and Winnowing, while C/C++/Java utilize variations of TF-IDF and Winnowing.)*

## Project Architecture

```text
codeguard/
├── backend/                  # FastAPI Application and Detection Engine
│   ├── auth.py               # JWT login & secure signup
│   ├── similarity.py         # Main similarity pipeline & Dataset Cache
│   ├── fingerprint.py        # Winnowing fingerprint algorithm implementation
│   ├── highlight.py          # Extracts matching block contexts 
│   ├── ast_similarity.py     # Source-code AST node tokenization
│   └── dataset/              # Default 500+ algorithm implementations
│
├── frontend/                 # React SPA
│   ├── src/                  # React components, Pages, and Hooks
│   ├── package.json          # Node dependencies
│   └── vite.config.js        # Vite bundler configuration
│
└── screenshots/              # Application UI snapshots
```

---

## Installation Guide

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure you have a running MongoDB instance (update connection strings in `backend/database.py` if necessary).
5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```

---

## Usage Instructions

1. Register for an account using a secure password (minimum 8 characters, letters & numbers).
2. Browse to the Upload page.
3. Upload a code file (e.g. `bubble_sort.py`).
4. Wait for the engine to compare your code against the internal dataset.
5. Review the deep-scan results, including the exact lines matched, the detected algorithm, and detailed similarity breakdown scores.

---

## Screenshots

### Code Upload & Analysis
![Upload Screen](screenshots/upload.png)

### Scan Results & Highlighted Plagiarism
![Results Screen](screenshots/results.png)

### Scan History Dashboard
![History Screen](screenshots/history.png)

---

## Future Improvements

* Add language-agnostic structural AST tokenization capabilities for Java and C++.
* Migrate the dataset cache to Redis for distributed system performance.
* Expand the algorithm families dataset to support dynamic user-submitted datasets.

## License

This project is licensed under the MIT License.
