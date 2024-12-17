def katta_harf_birinchi_belgi(satr):
    
    return satr[0].upper() + satr[1:].lower()

print(katta_harf_birinchi_belgi("salom"))     
print(katta_harf_birinchi_belgi("SALOM"))     
print(katta_harf_birinchi_belgi("sALoM"))
print(katta_harf_birinchi_belgi("dunyo"))      
