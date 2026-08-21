#!/usr/bin/env python3
"""Replace the footer markup with the new design across all HTML files.

New footer (matches the screenshot):
  - 4 columns: Logo+desc, Quick Links, Segments, Contact
  - Quick Links: Home, About Us, Products, Blog, Gallery, Career, Contact Us
  - Segments: Andrology/Sexology, Nephrology/Urology, IVF/Gynecology
  - Contact: Himeros Pharma, India  /  info@himerospharma.com
  - Bottom: copyright  +  'Crafted with care for healthcare professionals'
"""
import os
import re

LOGO_URL = "https://z-cdn-media.chatglm.cn/files/1a3ab43b-4646-4d32-8425-01926c3bf57e.png?auth_key=1881243185-e88cca88e5ab46839f86ff477a1e81dd-0-f6d45976647f27bf983575b3a7a94c23"

LINKEDIN_URL = "https://www.linkedin.com/company/himeros-pharma/posts/?feedView=all"
YOUTUBE_URL = "https://youtube.com/@himerospharma-n6p?si=vOHvi_RKTuSbyd07"
INSTAGRAM_URL = "https://www.instagram.com/himerospharma?igsi=MW01NDI5emR3YmduNQ%3D%3D&utm_source=qr"

NEW_FOOTER = '''<!-- Footer -->
    <footer class="bg-[#0b1f3a] text-white">
        <div class="max-w-7xl mx-auto px-4 pt-16 pb-8">
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
                <div>
                    <div class="footer-logo-wrap mb-5">
                        <img src="''' + LOGO_URL + '''"
                            alt="Himeros Pharma Logo" class="h-12 w-auto object-contain">
                    </div>
                    <p class="text-gray-300 text-sm leading-relaxed mb-6">Advancing pharmaceutical science for
                        better patient outcomes across specialties.</p>
                    <div class="flex gap-3">
                        <a href="''' + LINKEDIN_URL + '''" class="w-9 h-9 bg-white/10 rounded-lg flex items-center justify-center hover:bg-brand-600 transition-colors">
                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        </a>
                        <a href="''' + INSTAGRAM_URL + '''" class="w-9 h-9 bg-white/10 rounded-lg flex items-center justify-center hover:bg-brand-600 transition-colors">
                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>
                        <a href="''' + YOUTUBE_URL + '''" class="w-9 h-9 bg-white/10 rounded-lg flex items-center justify-center hover:bg-brand-600 transition-colors">
                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                        </a>
                    </div>
                </div>
                <div>
                    <h4 class="font-bold text-white mb-5 tracking-wider text-sm">QUICK LINKS</h4>
                    <ul class="space-y-3">
                        <li><a href="index.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Home</a></li>
                        <li><a href="about.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">About Us</a></li>
                        <li><a href="products.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Products</a></li>
                        <li><a href="blog.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Blog</a></li>
                        <li><a href="gallery.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Gallery</a></li>
                        <li><a href="career.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Career</a></li>
                        <li><a href="contact.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Contact Us</a>
                        </li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold text-white mb-5 tracking-wider text-sm">SEGMENTS</h4>
                    <ul class="space-y-3">
                        <li><a href="segment-andrology.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Andrology /
                                Sexology</a></li>
                        <li><a href="segment-nephrology.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">Nephrology /
                                Urology</a></li>
                        <li><a href="segment-gynecology.html"
                                class="text-gray-300 text-sm hover:text-green-400 transition-colors">IVF /
                                Gynecology</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold text-white mb-5 tracking-wider text-sm">CONTACT</h4>
                    <ul class="space-y-3">
                        <li class="flex items-start gap-3">
                            <span class="mt-0.5 text-green-400 flex-shrink-0">
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            </span>
                            <span class="text-gray-300 text-sm">Himeros Pharma, India</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="mt-0.5 text-green-400 flex-shrink-0">
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                            </span>
                            <a href="mailto:info@himerospharma.com" class="text-gray-300 text-sm hover:text-green-400 transition-colors">info@himerospharma.com</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-gray-400 text-sm">&copy; 2025 Himeros Pharma. All rights reserved.</p>
                <p class="text-gray-400 text-sm">Crafted with care for healthcare professionals</p>
            </div>
        </div>
    </footer>'''

count_updated = 0
count_skipped = 0

for filename in sorted(os.listdir('.')):
    if not filename.endswith('.html'):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the entire <footer>...</footer> block
    footer_match = re.search(r'(?:<!--\s*Footer\s*-->\s*)?<footer[\s\S]*?</footer>', content, re.IGNORECASE)
    if not footer_match:
        count_skipped += 1
        continue

    original = content
    content = content[:footer_match.start()] + NEW_FOOTER + content[footer_match.end():]

    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        count_updated += 1
    else:
        count_skipped += 1

print(f"Updated: {count_updated}")
print(f"Skipped: {count_skipped}")
