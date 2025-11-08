# Astarag Mohapatra — Profile Website

This repository now contains a fully static, multi-page portfolio for showcasing
projects, writing, coursework, and experience. Each major section of the profile is
available on its own HTML page for easier navigation and future updates.

## Getting started

Open `index.html` directly in your browser or serve the repository with any
static file host. Use the top navigation to jump to dedicated pages for projects,
writing, coursework, experience, and contact information. All styles and assets
are bundled locally under the `assets` directory.

## Deploying on GitHub Pages

You can publish the site with GitHub Pages in just a few clicks:

1. Push this repository to GitHub and open the project settings.
2. Under **Pages**, choose the branch you want to publish (for example, `main`) and set the
   deployment source to the repository root. Save the configuration.
3. Wait for GitHub Pages to build and deploy the site. Your portfolio will be available at
   `https://<username>.github.io/<repository>/` (or `https://<username>.github.io/` for a user site).

All navigation links and assets in the HTML files are relative paths (for example,
`projects.html` and `assets/css/styles.css`), so they resolve correctly regardless of whether the
site is hosted at the root domain or within a project subdirectory.

## Legacy Streamlit app

The previous Streamlit implementation is preserved in the `Introduction.py` file
and the `pages/` directory for reference.
