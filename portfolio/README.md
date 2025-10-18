n8n Automation Specialist — Client Portfolio

This folder contains a ready-to-share, single-page portfolio for an n8n specialist. Open index.html in any browser or host it as a static site.

Customize
- Open index.html and replace:
  - "Your Name" with your actual name
  - Contact details in the Contact section
  - Update Services, Case studies, and Pricing to match your offerings
- If you want a print/PDF one-pager, use your browser’s Print (Ctrl/Cmd+P).

Optional: Self-hosted details
- The Services section includes a minimal Docker Compose example for n8n self-hosting.
- Adjust environment variables and add a reverse proxy (Traefik/Nginx) for HTTPS in production.

Deploy options
- GitHub Pages: create a repo and enable Pages (main branch, /portfolio as root or move files to root)
- Netlify/Vercel: drag-and-drop the folder or connect the repo
- Any static host or S3 bucket will work

Structure
- index.html  — main page
- styles.css  — styling with dark theme and print-friendly layout

Notes
- No external dependencies or build steps
- Fully static, mobile responsive, and accessible without JS (JS is only used to render the year in the footer)
