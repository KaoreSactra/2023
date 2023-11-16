from youtube_transcript_api import YouTubeTranscriptApi as ytTranscript

# Main
outls = []

tx = ytTranscript.get_transcript('-HiQmZUmyXI', languages=['pt'])
for i in tx:
    outtxt = (i['text'])
    outls.append(outtxt)

    with open("op.txt", "a") as opf:
        opf.write(outtxt + "\n")

