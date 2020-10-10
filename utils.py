def display_side_by_side(dfs, captions):
    """
    Display tables side by side. dfs and captions are lists.
    Reference: 
        https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side/46345467
    """
    
    from IPython.display import display_html 
    
    output = ""
    combined = dict(zip(captions, dfs))
    
    for caption, df in combined.items():
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += '\xa0\xa0\xa0'
        
    display_html(output, raw = True)