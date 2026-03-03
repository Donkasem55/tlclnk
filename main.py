import sys, os
args = sys.argv[1:]
shorturl = args[-1]
args.pop()
ogurl = "%20".join(args)
os.mkdir(shorturl)
with open(f"{shorturl}/index.html", "w") as f:
	f.write(f"<!DOCTYPE html><html><head><title>REDIRECTING TO {ogurl}</title><meta http-equiv=\"refresh\" content=\"0; url={ogurl}\"></head><body><a href=\"{ogurl}\">If you are not redirected automatically, click this link</a></body></html>")
os.system("./push")
print(f"Created redirect https://donkasem55.github.io/tlclnk/{shorturl} which redirects to {ogurl}")
