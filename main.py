import sys, os
args = sys.argv[1:]
shorturl = args[-1]
args.pop()
ogurl = "%20".join(args)
os.mkdir(shorturl)
with open(f"{shorturl}/index.html", "w") as f:
	f.write(f"<!DOCTYPE html><html><head><title>REDIRECTING TO {ogurl}</title><meta http-equiv=\"refresh\" content=\"0; url={ogurl}\"></head><body><a href=\"{ogurl}\"><h1>REDIRECTING...</h1></a></body></html>")
with open("push") as f:
	for i in f.read().split("\n"):
		os.system(i)
print(f"Created redirect https://donkasem55.github.io/tlclnk/{shorturl} which redirects to {ogurl}")
