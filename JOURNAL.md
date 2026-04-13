<h1>Journal</h1>
Title: "Streambit"<br>
Author: "Aditya Roy(U04AKUFC402)"<br>
Description: "A 65% Keyboard made from scratch"<br>
Created On: "15/8/2025"<br>




I started from a layout for the keyboard, looking at designs like 100%, 85%, 70%, 65% and 65% looked the best to me.<br>
So, with some guides, I started with the schematic in KiCad 9.0.<br><br>

After placing everything systematically, it looked like this!

<img width="1368" height="759" alt="Screenshot 2025-07-23 at 6 18 33 PM" src="https://github.com/user-attachments/assets/15dbcae5-dcf8-485a-9bb0-eda0fcc9f81f" />
Time Spent: 30 mins<br>
<b>**Total time: 30 mins**<b>

<h3>Wiring Time!</h3>
After wiring every component in the schematic, it came out like this
<img width="1025" height="383" alt="Screenshot 2025-07-25 at 6 26 07 PM" src="https://github.com/user-attachments/assets/a7ae16ee-818f-41d7-a2f1-f8abe2177ca5" />
Time spent: 45 mins<br>
<b>**Total time: 1hr 15mins**</b>

<h2>Placing the components on the pcb</h2>
After turning the schematic into a PCB, I started placing the components on the PCB in order of the 65% keyboard I planned to make. Did not remember to get a screenshot of the process
Time spent: 1hr 30mins<br>
<b>**Total time: 2hr 45mins**</b>

<h2>Time to Route everything!</h2>
After finally placing the components with the correct spacing and order, I had to do the routings. It was a very long process and indeed took a very long time. I had to adjust the routings accordingly to be able to place vias, turn the layer while routing, leave space for the routes to change layers, and more.
<br>
Routing progress 
<img width="1144" height="529" alt="2" src="https://github.com/user-attachments/assets/983d93b1-eb91-45db-ae5b-c5efc4094451" />

Final Routed PCB<br>
<h6>Added Silkscreen also!</h6>
<img width="1098" height="496" alt="done" src="https://github.com/user-attachments/assets/2aa1ff19-589c-4523-88b2-334defa610fd" />
Time spent: 4hr 15mins<br>
<b>**Total time: 7hours**</b>


<h2>Case Designing Time!</h2>
For this case, I decided to use only a bottom case as an open PCB looks very beautiful. 
<h4>Creating Sketch!</h4>
<img width="1470" height="956" alt="Screenshot 2025-07-28 at 8 11 55 PM" src="https://github.com/user-attachments/assets/396f731f-6afa-47fe-9160-f2f8fde759fc" />

<h4>Adding holes for mount</h4>
<img width="1470" height="956" alt="Screenshot 2025-07-29 at 4 28 10 PM" src="https://github.com/user-attachments/assets/c95bbb52-6080-4445-895f-7ffe8dfcde25" />

After extruding the PCB, I made some designs on the sides of the case.<br>
Photo:<br>
<img width="1470" height="956" alt="Screenshot 2025-07-29 at 4 33 41 PM" src="https://github.com/user-attachments/assets/33c97eae-f7fd-4882-9df0-e67c99bc4e14" />

Video:<br>

https://github.com/user-attachments/assets/81f87b0e-f5fe-4575-91ca-c8a29a3c5382


<h3>Branding the Case!</h3><br>
<img width="1470" height="956" alt="Screenshot 2025-07-29 at 6 12 16 PM" src="https://github.com/user-attachments/assets/88d16f1a-feae-4cc4-9736-74f173f7306c" />

<h2>Case is Done!</h2><br>
<img width="1470" height="801" alt="Screenshot 2025-08-25 at 7 02 32 PM" src="https://github.com/user-attachments/assets/8b99cef6-925a-4ce8-b044-ac44f3446ba1" />
Time taken: 3hours
<b>**Total time: 10 hours**</b>

<h5>Gotta assemble everything physically now</h5><br>
<img width="1470" height="801" alt="Screenshot 2025-08-26 at 4 48 28 PM" src="https://github.com/user-attachments/assets/a7c23d15-0fe9-4a22-92d0-2fc387948749" />


<h3>Physical assembly time!</h3>
After getting all the components, I started by placing the diodes in place. In this, I had to bend each side of the diode to sit exactly in the centre of the logo, else it would have gone left or right while soldering.
<img alt="Diodes place" src="https://cdn.hackclub.com/019d8656-d220-70f6-a709-3ab7bd97e31f/all%20diodes%20place%20streambit.jpeg">
Time taken: 2hours
<b>Total Time: 12 hours</b>

<h4>Soldeing all diodes in place</h4>
After the placement session of the diodes was done, I had to solder them to the PCB and cut their long wires left. 
In this, I had to ensure that the diodes were placed correctly, else the resultant solder would have come out badly. 
Soldered results:<br>
Front
<img alt="Diodes front" src="https://cdn.hackclub.com/019d865e-0fae-7f99-916a-e8c8da27c06f/all%20diodes%20soldered%20front.jpeg">
Back
<img alt="Diodes back" src="https://cdn.hackclub.com/019d865e-0772-7b27-b680-4e25bebdd1a4/all%20diodes%20soldered%20back%20.jpeg">
Time taken: 1.5 hour
<b>Total time: 13.5 hours</b>

<h4>Soldering keys and joining stabs</h4>
After placing and soldering all of the 1N4148 diodes, I now had to solder my Cherry MX keys to the PCB. It was soooo fun, and it consumed 4 meters of soldering wire
Final look:<br>
<img src="https://cdn.hackclub.com/019d8667-26d9-76fd-ad05-407571050f9d/final%20soldered%20streambit.jpg">
Time taken: 3 hours
<b>Total time: 16.5 hours</b>

<h4>Solder Ras pi Pico</h4>
After being done with the 1N4148 diodes and Cherry MX switches, it was time to solder the last thing, which was the Raspberry Pi Pico to the PCB. Remember, the Ras pi pico was SMD, and I used a soldering iron for this job.
Final look:<br>
<img src="https://cdn.hackclub.com/019d866c-2644-78a7-a38d-62bfbb2eeee1/IMG_20260413_160743.jpg">
Time taken: 0.5 hours
<b>Total time: 17 hours</b>

<h3>Firmware time!!!</h3>
After being done with the soldering and things, I now had to upload the code to the Pico. I made many versions of the code coz the keys acted weird, rows and columns were wrongly arranged, and there were many bugs with the code.
<img width="1398" height="406" alt="image" src="https://github.com/user-attachments/assets/361b628d-2540-4041-ab4a-85933e0df902" />

Time taken: 6 hours
<b>Total time: 23 hours</b>
psst: two keys were placed wrongly dont mind :)
