
def match_par(c1,c2):
    return c1,c2=="(",")" or c1,c2=="{","}" or c1,c2=="[","]"

    

def Is_Valid_Paran(s):
    st=[]
    for char in s:
        if char in ["(","{","["]:
            st.append(char)
        else:
            if len(st)!=0 and match_par(char,st[-1]):
                st.pop()
    
    return len(st)==0
            
                
Is_Valid_Paran("[{()}][")

False
