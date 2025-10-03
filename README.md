# Astarag Mohapatra · Personal Site

This repository contains a static HTML and CSS version of my personal site. It replaces the previous Streamlit implementation with a lightweight, easily extensible front-end that can be hosted on any static site provider (GitHub Pages, Netlify, Vercel, etc.).

## Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/Athe-kunal/astarag_mohapatra.github.io.git
   cd astarag_mohapatra.github.io
   ```
2. Open `index.html` in your browser, or serve the site locally with any static file server:
   ```bash
   python -m http.server 8000
   ```
   Then visit <http://localhost:8000>.

## Structure

- `index.html` – landing page with an overview, featured highlights, and quick navigation to each section.
- `about.html` – personal backstory, motivations, and collaboration opportunities.
- `projects.html`, `blogs.html`, `courses.html`, `experiences.html` – content-rich subpages mirroring the original Streamlit tabs.
- `assets/css/styles.css` – global styles shared across all pages.
- `assets/js/site.js` – lightweight enhancements for navigation state and footer year updates.
- `assets/images/` – profile and project imagery used throughout the site.

## Customization

- Update the copy directly in the HTML files. Each section is grouped in semantic containers (`section`, `article`, `figure`) to keep edits straightforward.
- The design system (colors, typography, spacing) is defined with CSS custom properties at the top of `assets/css/styles.css` so the look and feel can be tuned from one place.
- To add a new page, duplicate an existing HTML file, update the `<title>`, and include a link in the navigation menu.

## Deployment

The site is static—no build step is required. Deploy by uploading the repository contents to your hosting provider of choice or by enabling GitHub Pages on the repository.
