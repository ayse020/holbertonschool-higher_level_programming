#!/usr/bin/env python3
"""
Templating Program Module
"""

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and list of attendees
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None: Creates output files or logs errors
    """
    # 1. Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    # 2. Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # 3. Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # 4. Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # 5. Check if all attendees are dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary")
            return
    
    # 6. Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Create a copy of the template
        invitation = template
        
        # Replace all placeholders
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            # Get value from dictionary
            value = attendee.get(key)
            
            # If value is None or empty, use "N/A"
            if value is None or str(value).strip() == "":
                value = "N/A"
            
            # Replace placeholder
            placeholder = f"{{{key}}}"
            invitation = invitation.replace(placeholder, str(value))
        
        # Create filename
        filename = f"output_{i}.txt"
        
        # Write to file
        with open(filename, 'w') as f:
            f.write(invitation)
        
        print(f"Created: {filename}")


# Test the function (this part won't run when imported)
if __name__ == "__main__":
    # Example template
    template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
    
    # Example attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", 
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", 
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", 
         "event_date": None, "event_location": "Boston"}
    ]
    
    # Test the function
    generate_invitations(template, attendees)
