import sys
import hashlib

def banner():
    print("\n|---- sha / md5 bruteforce ----|\n")

def lchck(arr, argarg):
    for i in range(len(arr)):
        if arr[i] == argarg:
            return True
    return False

def encrypt(enc, msg):
    if enc == "sha256":
        return hashlib.sha256(msg.encode()).hexdigest()
    elif enc == "md5":
        return hashlib.md5(msg.encode()).hexdigest()
    elif enc == "sha1":
        return hashlib.sha1(msg.encode()).hexdigest()
    
if __name__ == "__main__":
    banner()
    types = ["sha256", "sha1", "md5"]
    enctype      = sys.argv[len(sys.argv)-3]
    hashLoc      = sys.argv[len(sys.argv)-2]
    wordlistLoc  = sys.argv[len(sys.argv)-1]
    if not lchck(types, enctype):
        print("\n[!]\t\tno such encryption avaliable\n")
        exit()
    print(f"hashLoc:\t{hashLoc}\nwordlistLoc:\t{wordlistLoc}")
    hashfp = open(hashLoc, "r")
    hash = hashfp.readline().split("\n")[0]
    hashfp.close()
    print(f"hash:\t\t{hash}")
    with open(wordlistLoc, "r") as wordfp:
        end = False
        while True:
            tmp = wordfp.readline().split("\n")[0]
            if encrypt(enctype, tmp) == hash:
                print(f"plain:\t\t{tmp}\n")
                end = True
                break
            elif tmp == "":
                break
    if not end:
        print("[!]\t\tno password maches the hash\n")


