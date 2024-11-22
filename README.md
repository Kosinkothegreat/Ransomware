# Ransomware Simulation Tool  

## Overview  
This project is a **ransomware simulation tool** designed for **educational** and **research purposes only**. The tool demonstrates how ransomware operates by encrypting files on a target system, showcasing the potential impact and serving as a resource for developing defensive strategies.  

> **Warning**:  
> This tool is intended for use in controlled environments such as labs and should not be deployed on unauthorized systems. Misuse of this software may violate laws and ethical guidelines.  

---

## Features  
- **File Encryption**: Encrypts specified files or directories using a strong encryption algorithm.  
- **Custom Encryption Keys**: Allows integration with custom key management systems.  
- **Simulation-Only Mode**: Ensures no permanent data loss during testing.  
- **Logging**: Generates detailed logs of the encryption process for analysis.  
- **Cross-Platform Support**: Compatible with Windows, Linux, and macOS.  

---

## Use Cases  
- **Penetration Testing**: Simulate ransomware attacks to test the effectiveness of defensive mechanisms.  
- **Awareness Training**: Demonstrate the potential impact of ransomware to users and IT staff.  
- **Incident Response Development**: Enhance detection and mitigation strategies for ransomware incidents.  

---

## Installation  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/kosinkothegreat/Ransomware.git  
   cd <Ransomware>  
   ```  

2. **Set Up Dependencies**:  
   Install the required libraries:  
   ```bash  
   pip install -r requirements.txt
   or pip install python3
   pip install cryptography
   #pip install os#
   ```  

3. **Run the Tool**:  
   Execute the script in your testing environment:  
   ```bash  
   python3 ransomware_sim.py  
   ```  

---

## How It Works  
1. **File Targeting**: Identifies files based on extensions or directory paths.  
2. **Encryption**: Uses AES-256 encryption to encrypt files securely.  
3. **Simulation Mode**: Generates an encryption report without encrypting actual files (optional).  
4. **Key Handling**: Provides a unique decryption key per session for recovery.  

---

## Usage Notes  
- Always test in a controlled and isolated environment (e.g., a virtual machine).  
- Never use this tool on production systems or personal devices.  
- Ensure you have proper backups before initiating the simulation.  

---

## Ethical Disclaimer  
This tool was developed strictly for educational and defensive purposes. Unauthorized use is prohibited. The developers are not responsible for any misuse or legal implications arising from its use.  



## Contributions  
Contributions are welcome! Please open an issue or submit a pull request for improvements, additional features, or bug fixes.  



## License  
This project is licensed under the [MIT License](LICENSE).  

