class AddrBook(object):
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        self.city = "Beijing"

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def update_phone(self,newph):
        self.phone = newph
        print("Now,%s phone number is: %s" % (self.name,self.phone))

class EmplAddrBook(AddrBook):
    company = "Tarena"

    def __init__(self,nm,ph,em,eid):
        AddrBook.__init__(self,nm,ph)
        self.email = em
        self.eid = eid
        aaa = 10

    def get_email(self):
        return self.email

if __name__ == '__main__':
    bob = AddrBook("Bob Green","15011111111")
    alice = AddrBook("Alice Smith","14511111221")
    print ("%s:%s" % (bob.get_name(),bob.get_phone()))
    print ("%s,%s" % (alice.get_name(),alice.get_phone()))
    bob.update_phone("15555555555")
    print ("%s:%s" % (bob.get_name(),bob.get_phone()))
    luke = EmplAddrBook('luke li','18611111111',"luke.li@test.com","1088")
    print (EmplAddrBook.company)
    print (luke.company)
