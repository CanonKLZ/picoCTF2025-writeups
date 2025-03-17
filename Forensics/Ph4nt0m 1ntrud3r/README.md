![image](https://github.com/user-attachments/assets/9ccc277b-a460-49a2-abaa-770591d8fe70)

Hints:
1. Filter your packets to narrow down your search.
2. Attacks were done in timely manner.
3. Time is essential

Download the pcap file and open using WireShark.

![image](https://github.com/user-attachments/assets/fa1f15ae-a5e8-4914-9d9f-fc3af01f3c52)

Fortunately this is an easy pcap file challenge, only few rows, flag can be found easily.

From the hints given, we need to filter the packets and the scope we need to focus on is the timeline.

### Hence, first, sort the packet.

![image](https://github.com/user-attachments/assets/bcbe3e2d-065d-4a93-8ed6-6cc59de5a7eb)

Nice, now we know that the row with negative time value can be ignored.

Then the flag pieces are hidden in the records with positive time values.

![image](https://github.com/user-attachments/assets/0e413ace-cdfb-40f6-ac70-fa6e90c63a82)

Above shows the flag piece in record 1.

Do the same thing to the rest of the records: 10, 4, 18, 3, and 2.

Decode the flag pieces and get the complete flag.
