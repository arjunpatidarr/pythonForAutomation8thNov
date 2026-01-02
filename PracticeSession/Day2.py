
st = {}
st = {"101",34,2,4,"tg",23}
print(st)
print(st)
st.add(10)
print(st)
st.add("wdt")
print(st)
st.add("wsdr")
st.update("abc","wsd", "rdss")
print(st)
st.update([45,67,87])
print(st)

# remove data

st.remove("wsdr")
st.remove(23)
print(st)

st.add(101)
print(st)

#st.remove(1000)
st.discard("a")
print(st)

st.discard("wdtase")
print(st)

st.pop()
print(st)

st.pop()
print(st)
st.pop()
print(st)

st.pop()
print(st)


#copy list
st1 = st.copy()
print(st1)

print(len(st1))

#sorting

st2 = {12,4,5,6,7,8,33,45,44}
st3 = sorted(st2)
print(st3)

st3.reverse()
print(st3)


#clear
st3.clear()
print(st3)

#delete

del st3
#print(st3)

#convert set into list

print(st2)
st4 = list(st2)
print(st4)


