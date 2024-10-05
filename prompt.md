@./dsl2bash.py

at the end we're going to approval test ("verify") the frames
1. received file name should be session.frame.received
2. at the end, touch session.frame.approved
3. diff session.frame.received session.frame.approved
4. if different, launch diff tool, defult to vimdiff
5. if any frame verification fails, exit with 1
6. if all frames are verified, exit with 0, no diff tool launched


