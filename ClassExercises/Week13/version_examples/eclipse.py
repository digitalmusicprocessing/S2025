fin = open("eclipse.txt")
lines = [l.strip() for l in fin.readlines()]
fin.close()
lines = [l for l in lines if len(l) > 0]
i = 0
s = """<ul class="features">"""
while i < len(lines):
    labels = lines[i:i+3]
    html = lines[i+3:i+6]
    i += 6
    for k in range(3):
        s += """
                                        <li>
                                            <span class="solid major style1">{}</span>
                                            <p>
                                                {}
                                            </p>
                                        </li>
        """.format(labels[k], html[k])
s += "</ul>"
print(s)