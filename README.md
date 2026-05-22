<a name="top"></a>

<p align="center"> 
  <a href="https://www.linkedin.com/in/clarence-fong" target="_blank">
    <img width="50" height="50" alt="LinkedIn" src="https://github.com/user-attachments/assets/7ab6e12b-ca8a-4aa6-8f10-79ba89d485b5" />
  </a>
  <a href="mailto:abc1230940@gmail.com">
    <img width="50" height="50" alt="Gmail" src="https://github.com/user-attachments/assets/4e0491ce-239c-413c-b433-74a5ff48f231" />
  </a>
  <a href="https://www.instagram.com/cyberbrexel?igsh=MXNxeWJid2VxZWxxaw%3D%3D&utm_source=qr" target="_blank">
    <img width="50" height="50" alt="Instagram Old" src="https://github.com/user-attachments/assets/62e4672b-d424-4489-a204-c301040905a3" />
  </a>
  <a href="https://discordapp.com/users/cyberbrexel" target="_blank">
    <img width="50" height="50" alt="Discord" src="https://github.com/user-attachments/assets/f76173ca-fad3-4390-bca1-5c2305bc748e" />
  </a>
  <a href="https://www.reddit.com/user/abc1230940/" target="_blank">
    <img width="50" height="50" alt="Reddit" src="https://github.com/user-attachments/assets/6e9bd985-dfa3-4349-b966-4cf49362bd61" />
  </a>
</p> <br>


<h3 id="web-server-port-alerter "align="center"> 
  <strong> Web Server Port alerter </strong>
</h3>
<p align="center">
  <img width="200" height="200" alt="Port Scanner" src="https://github.com/user-attachments/assets/08d2fdf6-6da4-4731-a4a7-9eb2c552d03d" />
</p>


<p align="center">
  An automated Python tool that scans local web server ports every 1 hour and triggers automated alerts to send to Discord Webhook server
</p> <br>

<details>
  <summary>🔎 Table of Content</summary>
  <ol>
    <li> <a href="#about-the-project"> About The Project </a> </li>
    <ul>
    <li> <a href="#built-with"> Built With </a></li>
      <ul>
        <li> <a href="#language"> Language </a> </li>
        <li> <a href="#libraries-and-dependancies"> Libraries & Dependancies </a> </li>
      </ul>
    </ul>
    <li> <a href="#getting-started"> Getting Started </a> </li>
    <ul>
      <li> <a href="#prerequisites"> Prerequisites </a> </li>
      <li> <a href="#installation"> Installation </a> </li>
    </ul>
    <li> <a href="#usage"> Usage </a> </li>
    <li> <a href="#acknowledgement"> Acknowledgement </a> </li>
  </ol>
</details>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="about-the-project"> About the Project </h2>
<img width="845" height="62" alt="2 12" src="https://github.com/user-attachments/assets/b0743ece-d452-4e58-8231-a49f5cda9521" />
<p> Port scanning is a fundamental technique widely used by both <strong>Red Teams (Attackers)</strong> and <strong>Blue Teams (Defenders)</strong>. While offensive security teams use port scanners during the reconnaissance phase to discover active hosts and map out open entry points, defensive operations rely on them to audit network perimeters, detect unauthorized services, and identify potential vulnerabilities before they can be exploited. </p>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h3 id="built-with"> Built With </h3>
<h4 id="language"> Language </h4>
<img src="https://img.shields.io/badge/Python-14354C?style=plastic&logo=python&logoColor=white" />
<h4 id="libraries-and-dependancies"> Libraries & Dependancies </h4>
<ul>
 <li> certifi (v2.7.0) </li>
 <li> charset-normalizer (v3.4.7) </li>
 <li> idna (v3.15) </li>
 <li> requests (v2.34.2) </li>
 <li> urllib3 (v2.7.0) </li>
</ul>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="getting-started"> Getting Started </h2>
The web server port alerter is used on the unix system, please make sure the system is updated and python with virtual environment is installed. Moreover, A Discord Webhook server is required to install to receive alert notifications.
<h3 id="prerequisites"> Prerequisites </h3>
<p> 1. System Update and Installation of Python </p>
<pre> <code lang="bash"> sudo apt update && sudo apt install -y python3.12-venv </code> </pre>
<p> 2. Configurating a Discord Webhook Server </p>
<p> 2-1. Navigating to <a href="https://discord.com"> Discord </a> and Login </p>
<img width="1851" height="965" alt="2" src="https://github.com/user-attachments/assets/4ffcb751-461d-4d9d-bd9b-f5c570db63de" /><br>
<p> 2-2. Add a Server</p>
<img width="467" height="208" alt="2 0" src="https://github.com/user-attachments/assets/373f25c0-33a6-4195-b7ff-2d6040171e8c" /><br>
<p> 2-3. Create Your Server</p>
<p> choose "Create My Own" </p>
<img width="550" height="700" alt="2 1" src="https://github.com/user-attachments/assets/5d991dc8-1d4a-4fd8-94f0-02ec7c844cfd" /><br>
<p> 2-4. Tell Us About Your Server </p>
<p> choose "For me and my friends" </p>
<img width="548" height="465" alt="2 2" src="https://github.com/user-attachments/assets/fc8fe3bc-c7be-47f6-915d-33f621b0f742" /><br>
<p> 2-5. Customize Your Server </p>
<p> Give a name to your server and i named "Port Scanning" </p>
<img width="552" height="517" alt="2 3" src="https://github.com/user-attachments/assets/2d3f9904-fa44-4d64-a971-2a2866700383" /><br>
<p> 2-6. A server is installed </p>
<p> Click the Gear icon next to # general </p>
<img width="1503" height="821" alt="2 4" src="https://github.com/user-attachments/assets/8aeef7c3-6660-4663-9679-96c88d535915" /><br>
<p> 2-7. Click "Overview" </p>
<img width="322" height="293" alt="2 6" src="https://github.com/user-attachments/assets/9cbf5013-aa5a-4589-a794-bdf07ec93482" /><br>
<p> 2-8. Click "Create Webhook" button </p>
<img width="963" height="497" alt="2 7" src="https://github.com/user-attachments/assets/8696f10d-5717-45e7-9812-c900793bab44" /><br>
<img width="970" height="606" alt="2 8" src="https://github.com/user-attachments/assets/975b1735-aeb7-45d1-9b55-864bd0d8daf7" /><br>
<p> 2.9. Click "Copy Webhook URL" button and paste it to your clipboard </p>
<img width="873" height="523" alt="2 9" src="https://github.com/user-attachments/assets/fad75ac0-ec8d-470b-b27a-f9b459e27489" /><br>
<p> 2.10. Great! The Webhook server is created! </p>
<h3 id="installation"> Installation </h3>
<p> 1. Clone the Repo </p>
<pre> <code lang="bash">git clone https://github.com/abc1230940/web-server-port-alerter.git</code> </pre>
<p> 2. Navigate into the folder </p>
<pre> <code lang="bash">cd web-server-port-alerter</code> </pre> 
<p> 3. Set up the virtual environment </p>
<pre> <code lang="bash">python3 -m venv env</code> </pre>
<p> 4. Activate the virtual environment </p>
<pre> <code lang="bash">source env/bin/activate</code> </pre>
<p> 5. Install the required dependancies </p>
<pre> <code lang="bash">pip install -r requirements.txt</code> </pre>
<p> 6. Deactivate the virtual environment when finished </p>
<pre> <code lang="bash">deactivate </code> </pre>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="usage"> Usage </h2>
<p> 1. Edit the python script and then save</p>
<pre> <code lang="bash">nano alerter.py</code> </pre>
<img width="1502" height="832" alt="2 13" src="https://github.com/user-attachments/assets/6fee7b6c-7373-4e6c-94ca-2304af197d26" />
<p> ❗Since the alerter is used to scan our own web server, so change the IPv4 addresses to <strong>127.0.0.1</strong> and port to <strong>80, 443, 8080</strong> </p>
<p> ❗Paste your <strong>Webhook URL</strong> from the clipboard you have done before</p>
<p> 2. Launch the network port alerter script to begin monitoring </p>
<pre> <code lang="bash">python3 alerter.py</code> </pre>
<p> 3. If the targeted port was closed or service was down, the following alert will be shown </p>
<img width="845" height="62" alt="2 12" src="https://github.com/user-attachments/assets/9992c26f-5802-4c32-a91a-b2811bf76896" />
<p> 4. And the alert is also sent to your webhook server, so you can be alerted immediately on your workstation</p>
<img width="1103" height="125" alt="2 10" src="https://github.com/user-attachments/assets/50e20e1e-e0e1-4bc7-9511-0096cfaf5854" />
<p> 5. The alerter is run automatically for every hour (3600 seconds) to keep checking the operation of your server</p>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="acknowledgement"> Acknowledgement </h2>
<p> </p><a href="https://app.letsdefend.io/training/lessons/python-for-blue-team"> LetsDefend - Python for Blue Team </a> </p>
<p> </p><a href="https://discord.com"> Discord </a> </p> 
<img width="1506" height="786" alt="2 14" src="https://github.com/user-attachments/assets/0013778a-8ff6-4bcb-8bd2-e2789f523c59" />
<p align="right">(<a href="#top">Back to Top</a>)</p>



