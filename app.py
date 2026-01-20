from validator import validate_nigeria_id

print("🇳🇬 Nigeria Service ID Validator Demo\n")

while True:
    nid = input("Enter Nigeria Service ID (or 'q' to quit): ")
    if nid.lower() == "q":
        break

    if validate_nigeria_id(nid):
        print("✅ ID is valid!\n")
    else:
        print("❌ ID is invalid!\n")
