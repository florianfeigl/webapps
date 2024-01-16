#!/usr/bin/env python3

import os
import frontmatter

# Loading files from posts directory and render and parse relevant parameters
def load_posts(directory) -> list:
    posts = []
    # Get all markdown file paths and sort them
    file_paths = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')], reverse=True)

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as data:
            post = frontmatter.load(data)
            rendered_post = {
                'id': post.get('id', None),
                'title': post.get('title', 'No Title'),
                'date': post.get('date', 'No Date'),
                'body': post.content
            }
            posts.append(rendered_post)
            
    return posts

   
# Adds/removes quotes (") from elements
def clean_frontmatter(path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        in_front_matter = False
        for line in lines:
            if line.startswith('---'):
                in_front_matter = not in_front_matter
            elif in_front_matter and ':' in line:
                key, value = line.split(':', 1)
                value = value.strip()

                # Remove quotes from date fields if present
                if key.strip() == 'date' and (value.startswith(('"', "'")) and value.endswith(('"', "'"))):
                    value = value[1:-1]  # Remove the first and last characters (quotes)

                # Add quotes to non-date fields if not present
                elif not (value.startswith(('"', "'")) or key.strip() == 'date'):
                    value = f'"{value}"'

                line = f'{key}: {value}\n'
            
            file.write(line)
