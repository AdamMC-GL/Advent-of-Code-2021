t, lines = open('input.txt', 'r').read().split("\n\n")
lines = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in lines.split("\n")}


def day_14(r):
    c, m = {}, {}
    for i in t:
        c[i] = c.get(i, 0) + 1
    for i in range(len(t) - 1):
        m[t[i] + t[i + 1]] = m.get(t[i] + t[i + 1], 0) + 1

    for _ in range(r):
        m_ = dict(m)
        for i in m_:
            if i in lines and m_[i] > 0:
                c[lines[i]] = c.get(lines[i], 0) + m_[i]
                m[i[0] + lines[i]] = m.get(i[0] + lines[i], 0) + m_[i]
                m[lines[i] + i[1]] = m.get(lines[i] + i[1], 0) + m_[i]
                m[i] -= m_[i]

    print(max(c.values()) - min(c.values()))


day_14(10)  # Part 1
day_14(40)  # Part 2
