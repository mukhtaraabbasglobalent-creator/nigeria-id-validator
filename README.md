## Step 2: Nigeria ID Format & Validation Rules

This section defines the **Nigeria Service ID** format, demo state and registry codes, and validation rules for this project.

---

## 1️⃣ ID Format
| Part | Meaning | Example |
|------|---------|---------|
| NSV  | Fixed prefix (“Nigeria Service Validator”) | NSV |
| SS   | State code (01–37) | 05 (Lagos) |
| RR   | Registry/Agency code (01–99) | 03 (Social Services) |
| YYYY | Year of registration | 2026 |
| NNNN | Sequential number | 0001 |
| C    | Luhn checksum digit | 7 |

**Example full ID:**
---

### 2️⃣ Demo State Codes

| State Name        | Code |
|------------------|------|
| Lagos            | 05   |
| Abuja (FCT)      | 09   |
| Kano             | 14   |
| Rivers           | 23   |
| Oyo              | 28   |
| Kaduna           | 19   |
| Enugu            | 21   |

---

### 3️⃣ Demo Registry / Agency Codes

| Registry Name          | Code |
|-----------------------|------|
| Health                | 01   |
| Education             | 02   |
| Social Services       | 03   |
| Agriculture           | 04   |
| Trade / Export        | 05   |

---

### 4️⃣ Validation Rules

1. **Structure Check**
   - Must match format `NSV-SS-RR-YYYY-NNNN-C`  
   - Prefix must be `NSV`  

2. **State & Registry Codes**
   - SS must exist in `STATE_CODES`  
   - RR must exist in `REGISTRY_CODES`  

3. **Year & Sequence**
   - YYYY must be between 2020–2026 (for demo)  
   - NNNN must be 0001–9999  

4. **Checksum Check**
   - Remove letters/dashes → digits only  
   - Apply **Luhn algorithm** to verify last digit  

---

### 5️⃣ Example Demo IDs

| Example ID                  | Meaning |
|------------------------------|---------|
| NSV-05-01-2026-0001-?       | Lagos, Health, 2026, first record |
| NSV-09-02-2025-0123-?       | Abuja, Education, 2025, record 123 |
| NSV-14-05-2026-0456-?       | Kano, Trade/Export, 2026, record 456 |

> The `?` will be replaced by the **Luhn checksum digit** in code.

---

**Note:** This is a **demo project**. The Luhn algorithm only detects input errors, not fraud. Real systems require **security layers** such as encryption, authentication, and logging.
# nigeria-id-validator
Nigeria-focused ID validation demo using checksum algorithms
# 🇳🇬 Nigeria ID Validator (Demo Project)

## Purpose
This project demonstrates how **checksum algorithms** (specifically the Luhn algorithm) can be used to reduce data-entry errors in national-scale identification or service systems in Nigeria.

## Why This Project
Many digital systems fail due to simple human input errors.  
This project shows how basic validation improves reliability — while also explaining why validation alone is **not security**.

## Scope
- Structured Nigeria-focused ID format
- Checksum validation using Luhn
- Clear discussion of security limitations

> ⚠️ This is a demo project, not an official government system.

## Author
Mukhtar Aliyu
