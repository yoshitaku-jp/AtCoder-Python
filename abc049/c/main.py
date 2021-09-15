s = input()


while 1:
    for frag in ("erase", "eraser", "dream", "dreamer"):
        if s.endswith(frag):
            s = s[: -len(frag)]
            break
    else:
        print("NO")
        break
    if not s:
        print("YES")
        break
