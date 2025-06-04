 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/main.py
index 0000000000000000000000000000000000000000..16dbe00ad99b1479b121d6a903bd2445415289af 100644
--- a//dev/null
+++ b/main.py
@@ -0,0 +1,88 @@
+import json
+import os
+
+# Chuong trinh quan ly danh ba su dung tep JSON
+
+# Ten tep luu tru danh ba
+CONTACTS_FILE = 'contacts.json'
+
+# Ham doc danh ba tu tep
+def load_contacts():
+    if not os.path.exists(CONTACTS_FILE):
+        return []
+    with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
+        try:
+            return json.load(f)
+        except json.JSONDecodeError:
+            return []
+
+# Ham ghi danh ba vao tep
+def save_contacts(contacts):
+    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
+        json.dump(contacts, f, indent=2)
+
+# Ham them lien he moi
+def add_contact(contacts):
+    name = input('Name: ').strip()
+    phone = input('Phone: ').strip()
+    email = input('Email: ').strip()
+    contacts.append({'name': name, 'phone': phone, 'email': email})
+    save_contacts(contacts)
+    print('Contact added.')
+
+# Ham hien thi tat ca lien he
+def view_contacts(contacts):
+    if not contacts:
+        print('No contacts found.')
+        return
+    for idx, c in enumerate(contacts, 1):
+        print(f"{idx}. {c['name']} - {c['phone']} - {c['email']}")
+
+# Ham tim kiem lien he theo ten
+def search_contacts(contacts):
+    query = input('Search by name: ').strip().lower()
+    results = [c for c in contacts if query in c['name'].lower()]
+    if results:
+        for c in results:
+            print(f"{c['name']} - {c['phone']} - {c['email']}")
+    else:
+        print('No matching contacts found.')
+
+# Ham xoa lien he
+def delete_contact(contacts):
+    name = input('Name of contact to delete: ').strip().lower()
+    before = len(contacts)
+    contacts[:] = [c for c in contacts if c['name'].lower() != name]
+    if len(contacts) < before:
+        save_contacts(contacts)
+        print('Contact deleted.')
+    else:
+        print('Contact not found.')
+
+# Ham chinh chay menu quan ly danh ba
+def main():
+    contacts = load_contacts()
+    while True:
+        print('\nContact Manager')
+        print('1. Add contact')
+        print('2. View contacts')
+        print('3. Search contact')
+        print('4. Delete contact')
+        print('5. Exit')
+        choice = input('Choose an option: ').strip()
+        if choice == '1':
+            add_contact(contacts)
+        elif choice == '2':
+            view_contacts(contacts)
+        elif choice == '3':
+            search_contacts(contacts)
+        elif choice == '4':
+            delete_contact(contacts)
+        elif choice == '5':
+            break
+        else:
+            print('Invalid choice. Please try again.')
+
+# Khoi chay chuong trinh
+if __name__ == '__main__':
+    main()
 
EOF
)
