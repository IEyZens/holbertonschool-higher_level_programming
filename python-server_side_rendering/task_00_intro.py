def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Invalid input: template should be a string.")
        return
    elif not isinstance(attendees, list):
        print("Invalid input: attendees should be a list of dictionaries.")
        return
    elif not template:
        print("Template is empty, no output files generated.")
        return
    elif not attendees:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):

        invitation = template

        name = person.get("name") or "N/A"
        invitation = invitation.replace("{name}", name)

        event_title = person.get("event_title") or "N/A"
        invitation = invitation.replace("{event_title}", event_title)

        event_date = person.get("event_date") or "N/A"
        invitation = invitation.replace("{event_date}", event_date)

        event_location = person.get("event_location") or "N/A"
        invitation = invitation.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(invitation)
