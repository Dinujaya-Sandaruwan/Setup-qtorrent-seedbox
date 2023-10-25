# How to Set Up uTorrent Server on a Ubuntu VPS and Download Files

uTorrent Server is a BitTorrent client that can be installed on a Ubuntu Virtual Private Server (VPS). This guide will walk you through the process of setting up uTorrent Server on your VPS and downloading files to your local computer.

## Prerequisites

- A Ubuntu VPS with root access.
- Basic knowledge of working with the command line.

## Step 1: Connect to Your VPS

Access your VPS using SSH:

```bash
ssh root@your_server_ip
```

## Step 2: Update Your System

Update the package list to ensure your system has the latest software information:

```bash
apt update
apt upgrade
```

## Step 3: Install Dependencies

Install the required library dependencies:

```bash
sudo -i
echo "deb http://security.ubuntu.com/ubuntu/ bionic-security main" >> /etc/apt/sources.list
sudo apt update && apt-cache policy libssl1.0.0

apt-get install libssl1.0.0 libssl-dev

```

## Step 4: Download and Install uTorrent Server

Download and extract uTorrent Server to the `/opt` directory:

```bash
# Download the appropriate version for your system architecture.
# Replace the URL with the correct one if necessary.
wget http://download-new.utorrent.com/endpoint/utserver/os/linux-x64-ubuntu-13-04/track/beta/ -O utorrent.tar.gz

# Extract the downloaded archive to /opt.
tar -zxvf utorrent.tar.gz -C /opt/
```

## Step 5: Start uTorrent Server

Start uTorrent Server with the following command:

```bash
/opt/utorrent-server-alpha-v3_3/utserver -settingspath /opt/utorrent-server-alpha-v3_3/ &
```

## Step 6: Access the Web User Interface

Open a web browser and navigate to your VPS's IP address on port 8080:

```
http://xx.xx.xx.xx:8080/gui/web/index.html
```

## Step 7: Add a Magnet Link

- Log in to the Web UI using your username (admin) and password (none).
- Look for an option to add a new torrent, often labeled as "Add Torrent" or "Add URL."
- Paste the magnet link and initiate the addition process.

## Step 8: Download Files to Your Local Computer

- In the Web UI, locate the torrent you added.
- Click on the torrent's name to open its details page.
- Find the download button or option, and click it.
- uTorrent Server will start downloading the files associated with that torrent to your local computer. Choose a location on your local computer to save the files.

Enjoy downloading files from uTorrent Server on your VPS to your local computer!
