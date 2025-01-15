# Gui-password-generator-with-inbuild-password-manager-
# Password Generator & Manager

This is a powerful and user-friendly **Password Generator and Manager** built using Python and Tkinter. It allows users to create secure passwords of customizable lengths, save them for different services, and retrieve them whenever needed. The application is designed with a high-quality graphical user interface (GUI) for seamless interaction and functionality.

---

## Features

### 1. **Password Generator**
   - Create secure passwords with a mix of uppercase and lowercase letters, digits, and special characters.
   - Users can specify the desired password length to ensure it meets their security requirements.

### 2. **Password Manager**
   - Save generated passwords along with the associated service name.
   - Passwords are stored securely in a local JSON file for easy retrieval and management.

### 3. **View Saved Passwords**
   - Display all stored passwords in a clean, organized format.
   - Retrieve your passwords when needed without searching through files.

### 4. **Intuitive GUI**
   - Built using Python’s `Tkinter` library for a responsive and visually appealing interface.
   - Easy-to-navigate layout with labeled sections for each function.

---

## How It Works

1. **Generate a Password**:
   - Enter the desired password length in the "Password Length" field.
   - Click the "Generate Password" button to create a random password, which will appear in the "Generated Password" field.

2. **Save a Password**:
   - Enter the name of the service (e.g., "Email", "GitHub", "Bank Account") in the "Service Name" field.
   - Click the "Save Password" button to store the password securely in a JSON file.

3. **View Saved Passwords**:
   - Click the "View Passwords" button to see a list of all saved passwords along with their associated service names.
   - Saved passwords are displayed in a popup window for quick access.

---

## File Structure

- `passwords.json`: A local file where all the saved passwords are securely stored in JSON format.

---

## Requirements

- Python 3.x
- `tkinter` (pre-installed with Python)
- No external libraries are required, making this application lightweight and easy to set up.

---

## Installation and Usage

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/password-generator-manager.git
cd password-generator-manager
```

### **2. Run the Script**
```bash
python password_manager.py
```

### **3. Start Using the Application**
   - Generate secure passwords.
   - Save them with a service name.
   - View and manage your saved passwords.

---

## Code Walkthrough

### **Password Generation**
The `generate_password` function creates a secure password based on the specified length. It uses Python’s `random` and `string` modules to include:
- Uppercase and lowercase letters.
- Digits.
- Special characters.

### **Password Storage**
The `save_password` function saves passwords in a structured JSON file (`passwords.json`). Each password is associated with a unique service name.

### **View Saved Passwords**
The `view_passwords` function reads from the `passwords.json` file and displays the stored passwords in a popup message box.

### **Error Handling**
- If an invalid password length is entered, the application displays an error message.
- If the "Service Name" or "Password" field is empty, users are alerted to provide the necessary input.

---

## User Interface Design

- **Service Name Field**: A text entry box for entering the name of the service (e.g., "Facebook", "Twitter").
- **Password Length Field**: A numeric entry box for specifying the desired password length.
- **Generated Password Field**: A read-only field where the generated password is displayed.
- **Buttons**:
  - **Generate Password**: Creates a new password.
  - **Save Password**: Saves the password for the given service.
  - **View Passwords**: Displays all saved passwords in a popup.

---

## Security Considerations

- Passwords are stored locally in a JSON file. While this is convenient, users should ensure the `passwords.json` file is stored securely and not shared.
- For added security, consider encrypting the JSON file using libraries like `cryptography` or `pycryptodome`.

---

## Possible Improvements (Future Updates)

- **Password Encryption**: Encrypt the saved passwords for enhanced security.
- **Search Functionality**: Allow users to search for passwords by service name.
- **Export and Import**: Add functionality to export passwords to a file or import them into another device.
- **Dark Mode**: Add a dark mode option for better usability in low-light conditions.
- **Multi-Language Support**: Support for multiple languages in the GUI.

---

## Contribution Guidelines

We welcome contributions! If you'd like to contribute to this project:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to:
- The Python community for their incredible resources and support.
- Developers who contributed to the evolution of GUI applications using Tkinter.

---

Feel free to copy, modify, and use this project to suit your needs. Let me know if you encounter any issues or have suggestions for improvement!
