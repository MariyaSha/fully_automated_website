# 👹 Fully Automated News Website 👹

**Tech Goblin** is a Streamlit news website that updates itself using n8n. RSS feeds provide new stories, AI decides which ones are worth publishing and writes new articles, and the workflow saves them to articles.json for the website to display.

## 🎥 Video Tutorial

In my **Python Simplified** tutorial, I show how to set up the website, publish it on a VPS, and automate new articles with n8n. The project files are provided here, so you can follow along.

<a href="" target="_blank">**Build a Website That Updates Itself with AI, n8n & Python 🐍🤖**</a>

<a href="" target="_blank"><img width="600" alt="Build a Website That Updates Itself with AI, n8n and Python" src="https://github.com/user-attachments/assets/d8b6e6ec-ff8b-48e1-8f61-5a407787e696"/></a>

## 🧪 1. Test Locally

From the project folder, with Docker running:

```bash
docker build -t tech-goblin .
docker run -p 8501:8501 tech-goblin
```

Open **http://localhost:8501**.

## 🚀 2. Publish on a VPS

Use a VPS with Docker and n8n installed (the video uses Hostinger KVM 2).

On the VPS, connect over SSH and create the project folder:

```bash
ssh root@YOUR_VPS_IP
mkdir tech-goblin
cd tech-goblin
```

In a **separate local terminal**, inside the project folder, copy the three website files:

```bash
scp app.py articles.json Dockerfile root@YOUR_VPS_IP:tech-goblin/
```

Back in the **VPS terminal**, build and run the website:

```bash
docker build -t tech-goblin .
docker run -d --restart unless-stopped -p 8501:8501 -v "$PWD:/app" tech-goblin
```

Your website is now accessible at **http://YOUR_VPS_IP:8501**.

## 🔌 3. Connect n8n to the Website

On the VPS, identify the n8n container and its user:

```bash
docker ps
docker exec YOUR_N8N_CONTAINER_NAME id
chown 1000:1000 /root/tech-goblin/articles.json
```

The tutorial's n8n user is `1000:1000`; replace this if your `id` output differs.

In **Hostinger → Docker Manager → n8n → Manage**, add this volume and redeploy:

```text
/root/tech-goblin/articles.json:/home/node/.n8n-files/articles.json
```

In n8n, use `/home/node/.n8n-files/articles.json` in both **Read/Write Files from Disk** nodes. Build and test the workflow as shown in the video, then click **Publish**.

## 🧠 4. n8n Resources

The [`n8n_resources`](n8n_resources/) folder contains the **two AI prompts and JavaScript code** used in the workflow shown in the video tutorial:

- **Basic LLM Chain** (after Edit Fields): scores news stories from 1–10 and explains the score.
- **Basic LLM Chain1** (after the If node): writes an article about a story approved for publishing.
- **Script / Code in JavaScript** (after Extract from File): adds the new article to `articles.json`, skipping duplicate source links.

![n8n workflow overview](https://github.com/user-attachments/assets/ae3ef40d-ef52-4259-8f5a-a7a8a436e4ff)

*This screenshot shows extra RSS feeds; the video tutorial uses three.*
