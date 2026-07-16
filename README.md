# File Integrity Checker

A command-line Python application that verifies whether target files have been modified by generating and comparing cryptographic SHA-256 hashes.


## Overview

File integrity monitoring is a core cybersecurity practice used to detect unauthorized changes to data. This tool computes baseline SHA-256 hashes for specified files, stores them, and compares active files against stored values to detect tampering or accidental modification.

## Features

* **Hash Generation:** Compute and store SHA-256 hashes for any local file.
* **Integrity Verification:** Compare active files against saved baseline hashes.
* **Tampering Detection:** Instantly identify byte-level modifications.
* **Error Handling:** Gracefully handles missing files and invalid paths.
* **Zero Dependencies:** Built entirely using Python standard libraries.

## Tech Stack

* **Language:** Python 3.x
* **Core Modules:** `hashlib` (cryptographic hashing), `os` (file system operations)

## Project Structure

```text
file-integrity-checker/
│
├── main.py          # Application logic and menu interface
├── sample.txt       # Target file for testing
├── hashes.txt       # Stored baseline hashes
└── README.md        # Project documentation

```

---

## Quick Start

### Prerequisites

* Python 3.6 or higher installed.

### Execution

1. Clone or download this repository.
2. Navigate to the project directory:

```bash
cd file-integrity-checker

```

3. Run the application:

```bash
python main.py

```

---

## Usage Example

### Verifying an Unmodified File

```text
==============================
   FILE INTEGRITY CHECKER
==============================

1. Generate Hash
2. Verify File
3. Exit

Choose an option: 2

Enter file name: sample.txt

[SUCCESS] File integrity verified. No changes detected.

```

### Verifying a Modified File

```text
Enter file name: sample.txt

[WARNING] Hash mismatch detected! The file has been modified.

```

---

## Cybersecurity Concepts Applied

* **Data Integrity:** Ensuring information remains accurate and unaltered during storage or transfer.
* **Cryptographic Hashing:** Utilizing SHA-256 one-way functions to produce unique fixed-length signatures for file contents.
* **Baseline Verification:** Comparing current system state against a trusted reference state.

---

## Roadmap

* Add support for alternate hashing algorithms (SHA-512, MD5).
* Transition baseline storage from plain text (`hashes.txt`) to structured JSON.
* Implement directory-level monitoring for batch checks.
* Develop a graphical interface (GUI) using Tkinter.

---

## License

Distributed under the MIT License. Free for educational and non-commercial use.