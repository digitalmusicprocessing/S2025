
row = """
<tr>
<td>
    <iframe width="250" height="100" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</td>
<td>
    <iframe width="250" height="100" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</td>
</tr>
"""

row = """

								<ul class="features">
									<li>
										<span class="solid major style1"></span>
										<p>
                                            <iframe width="250" height="100" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
										</p>
									</li>
									<li>
										<span class="solid major style1"></span>
										<p>
                                            <iframe width="250" height="100" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
										</p>
									</li>
								</ul>
"""

#versions = ["clBw3cWgPnE", "PNQeBXtUdgc", "Wh1J3mfimBc", "Kv55jFmyBKU", "s7498yydPo4", "AGxB21tp6Xo", "hoCwQdLq93w", "s7498yydPo4", "lpkqQno0AaU", "24VOo7-ctKU", "9LZ3NvKu524", "WN0UHG420GU", "hKmQ9GmbCRY", "FeqgguMjmQU"]

#versions = ["-uJ61jgFCMM", "xXvPFsoNnD4", "6J_48nvjWcs", "yZEYJh99bpE", "VQPisuKnVK8", "g8PBvaTRwjU", "SPSdG0N3qAk", "7nPBAiE76qY", "mmwic9kFx2c", "SnsGKSHvcnI", "hlo-8h9RuBA", "cg0fEE9wnuw", "yuZ6ro1d3yA", "wWMp4zXB_CY", "MkLdUp9jRmg", "38JpVRZwHi0"]

#versions = ["bRrVMte9IQQ","7nPBAiE76qY","umW5bqvihWY","6gGGAXmDd08"," tPQD4NzWh-E","nOXPM1l-nbc","zBZSEfLvmQI","cv4PsScEtuU","uWP9Nv6DUsg","ejvar9V9cOQ","3-M9AklLtAA","MUxl9ftwuOA"]

versions = ["TuzEn7E2g28","E-pv1iVXdAs","UX25exUP5gA","CD8bW1rWqOA","pFrTXGEmU2Q","3IOD9SqSfY4","Pju4NBDgEjI","lo7_cv6uv6M"]




s = ""
for i in range(0, len(versions), 2):
    s += row.format(versions[i], versions[i+1])

print(s)
