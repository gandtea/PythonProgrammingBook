# Pickle it
# Demonstrates pickling and shelving data

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

f = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f) # Must do in the correct order (same as you put in)
shape = pickle.load(f)   # i.e. it doesn't know the first one is 'variety'.
brand = pickle.load(f)


print("variety -", variety)
print("shape -", shape)
print("brand -", brand)
f.close()

print("\nShelving lists.") # Acts similarly to a dictionary.
s = shelve.open("pickles2.dat")

s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s["types"] = ["variety", "shape", "brand"]

s.sync() # make sure data is written

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
print(s)

s.close()

input("\n\nPress the enter key to exit.")
