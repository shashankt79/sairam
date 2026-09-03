╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                  🚀 REPLIT DEPLOYMENT - CLEAR STEPS                        ║
║                                                                            ║
║          Sept 2, 2026 | Limits Reset | 12 Minutes to Live Backend        ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


⚡ COMPLETE WALKTHROUGH (Follow Step-by-Step)
────────────────────────────────────────────────────────────────────────────

Your files are ready:
  ✓ app.py (updated with 0.0.0.0 binding)
  ✓ xgboost_model.pkl (1.2 MB, trained)
  ✓ requirements.txt (ready to copy)

Time needed: 15 minutes
Result: Live API at https://[your-url].repl.co


════════════════════════════════════════════════════════════════════════════

STEP 1: CREATE NEW REPL
═══════════════════════════════════════════════════════════════════════════

1. Open: https://replit.com in your browser
2. Login to your account
3. Click the blue "+ Create" button (top left corner)
4. Choose Python (language selector)
5. Click "Create Repl" button
6. Wait 30 seconds for environment to load
7. You'll see a blank coding area

✅ CHECK: You see a blank editor with "main.py" file


════════════════════════════════════════════════════════════════════════════

STEP 2: CREATE requirements.txt
═══════════════════════════════════════════════════════════════════════════

1. On LEFT SIDEBAR, look for the file list area
2. Click the folder icon or "Files" tab
3. Look for a "+" icon to create new file
4. Click it and type: requirements.txt
5. Press Enter/Return

Now copy-paste this EXACTLY into requirements.txt:

─────────────────────────────────────────────────────────────────────────
flask
scikit-learn
xgboost
pandas
numpy
─────────────────────────────────────────────────────────────────────────

6. Save file: Ctrl+S (or Cmd+S on Mac)

✅ CHECK: File appears in left sidebar as "requirements.txt"


════════════════════════════════════════════════════════════════════════════

STEP 3: DELETE main.py (IMPORTANT)
═══════════════════════════════════════════════════════════════════════════

1. In the FILES list on left, find "main.py"
2. Right-click on it
3. Click "Delete"
4. This prevents Replit from running the wrong file

✅ CHECK: main.py is gone from file list


════════════════════════════════════════════════════════════════════════════

STEP 4: UPLOAD app.py
═══════════════════════════════════════════════════════════════════════════

1. Look in FILES area for "Upload" button (or drag-drop zone)
2. Click "Upload files"
3. Navigate to: C:\Users\thont\Desktop\sairam-ai\
4. Select: app.py
5. Click Open/Upload
6. Wait for upload to complete

✅ CHECK: app.py appears in FILES list on left


════════════════════════════════════════════════════════════════════════════

STEP 5: UPLOAD xgboost_model.pkl
═══════════════════════════════════════════════════════════════════════════

1. Click "Upload files" again
2. Navigate to: C:\Users\thont\Desktop\sairam-ai\
3. Select: xgboost_model.pkl (1.2 MB file)
4. Click Open/Upload
5. Wait for upload to complete (may take 10-20 seconds for large file)

✅ CHECK: xgboost_model.pkl appears in FILES list


════════════════════════════════════════════════════════════════════════════

STEP 6: OPEN SHELL
═══════════════════════════════════════════════════════════════════════════

1. At the BOTTOM of the screen, find tabs (usually shows "Console", "Shell", etc.)
2. Click the "Shell" tab
3. You'll see a black terminal area with a $ prompt

✅ CHECK: You see $ prompt in terminal


════════════════════════════════════════════════════════════════════════════

STEP 7: INSTALL DEPENDENCIES
═══════════════════════════════════════════════════════════════════════════

1. Type this command in Shell (copy-paste to avoid typos):

pip install -r requirements.txt

2. Press Enter
3. Wait for installation (lots of text will scroll)
4. This takes 30-60 seconds

Expected output:
  ✓ You'll see: "Successfully installed flask pandas numpy..."
  ✓ $ prompt returns

If you see errors about pip, run:
  pip install --upgrade pip
  pip install -r requirements.txt

✅ CHECK: Installation completes without red errors


════════════════════════════════════════════════════════════════════════════

STEP 8: RUN app.py
═══════════════════════════════════════════════════════════════════════════

1. In Shell, type:

python app.py

2. Press Enter
3. Watch the output

You should see:
─────────────────────────────────────────────────────────────────────────
============================================================
🚀 SAIL FREIGHT FORECASTING DASHBOARD
============================================================
   🌐 Running on: http://0.0.0.0:8080
   📊 Accuracy: 86.1%
   💡 Press Ctrl+C to stop
============================================================
─────────────────────────────────────────────────────────────────────────

✅ CHECK: You see this banner output (exact port may vary)


════════════════════════════════════════════════════════════════════════════

STEP 9: GET PUBLIC URL
═══════════════════════════════════════════════════════════════════════════

1. Look at the TOP of the Replit window
2. You'll see a box/preview pane labeled "Webview" or showing a URL
3. It will show something like:

   https://sairam-ai-freight.replit.dev

Or:

   https://[projectname].[username].repl.co

4. Copy this URL (it's your public address)
5. This URL is accessible from anywhere

✅ CHECK: You have a working https:// URL


════════════════════════════════════════════════════════════════════════════

STEP 10: TEST THE DASHBOARD
═══════════════════════════════════════════════════════════════════════════

1. Open a NEW browser tab
2. Paste your Replit URL from STEP 9
3. Press Enter
4. Wait 2-3 seconds for page to load

You should see:
  ✓ Blue header: "🚢 SAIL - Freight Rate Forecasting System"
  ✓ 4 stat boxes (showing 86.1%, ₹175 Cr, etc.)
  ✓ Left side: Form with inputs
  ✓ Right side: Empty chart

5. Test the form:
   - Enter "Volume": 12000
   - Enter "Current Freight Rate": 11.50
   - Enter "Coal Price": 120
   - Enter "Oil Price": 80
   - Select "Month": August
   - Click "Get AI Recommendation" button

6. Expected result:
   ✓ Chart updates with forecast
   ✓ Recommendation box appears
   ✓ Shows "WAIT" or "CHARTER NOW"
   ✓ Displays potential savings

✅ CHECK: Dashboard works and predictions update


════════════════════════════════════════════════════════════════════════════

STEP 11: SHARE WITH TEAM
═══════════════════════════════════════════════════════════════════════════

1. Copy your public URL from STEP 9
2. Send to team on WhatsApp/Slack:

"🎉 BACKEND IS LIVE!

Dashboard: https://[your-url]

Everyone test it now:
- Enter different freight rates
- See predictions update
- Check recommendations
- This is the live API endpoint!"

3. Team members can:
   - Open URL on phone or computer
   - Test predictions
   - Use for demo video
   - Verify it's working


════════════════════════════════════════════════════════════════════════════

✅ FINAL VERIFICATION CHECKLIST
════════════════════════════════════════════════════════════════════════════

After completing all steps, verify each:

☐ All files uploaded to Replit (app.py, xgboost_model.pkl, requirements.txt)
☐ Shell shows: "Running on: http://0.0.0.0:8080"
☐ Public URL is accessible in browser
☐ Dashboard appears with blue header and stat boxes
☐ Form inputs work (can type values)
☐ "Get AI Recommendation" button is clickable
☐ Chart displays and updates when you click button
☐ Recommendation text appears (WAIT or CHARTER NOW)
☐ Different inputs give different recommendations
☐ Team can access URL from phone/other computer

If ALL checked: ✅ DEPLOYMENT SUCCESSFUL! 🎉


════════════════════════════════════════════════════════════════════════════

🆘 TROUBLESHOOTING
════════════════════════════════════════════════════════════════════════════

PROBLEM: "ModuleNotFoundError: No module named 'flask'"
─────────────────────────────────────────────────────────
FIX:
1. Go back to Shell
2. Run: pip install flask scikit-learn xgboost pandas numpy
3. Wait for completion
4. Run: python app.py again


PROBLEM: "FileNotFoundError: xgboost_model.pkl"
─────────────────────────────────────────────────────
FIX:
1. Check FILES list - is xgboost_model.pkl there?
2. If not, upload it again (STEP 5)
3. Make sure filename is EXACTLY: xgboost_model.pkl
4. Try running again: python app.py


PROBLEM: "Address already in use" or error with port
─────────────────────────────────────────────────────
FIX:
1. In Shell, press Ctrl+C to stop Flask
2. Wait 3 seconds
3. Run again: python app.py


PROBLEM: "Dashboard appears blank" or "won't load"
─────────────────────────────────────────────────────
FIX:
1. Check Shell for red error messages
2. Make sure Flask is running (should show the banner)
3. Hard refresh browser: Ctrl+Shift+R (or Cmd+Shift+R)
4. Try opening URL in a new incognito window
5. Check console for JavaScript errors (F12 → Console tab)


PROBLEM: "Predictions don't update" or "button doesn't work"
─────────────────────────────────────────────────────────────
FIX:
1. Refresh page: F5 or Ctrl+R
2. Try entering different values
3. Check browser console: F12
4. Look for JavaScript errors
5. Try clicking button again


════════════════════════════════════════════════════════════════════════════

📊 WHAT YOU GET AFTER DEPLOYMENT
════════════════════════════════════════════════════════════════════════════

1. PUBLIC URL
   └─ Share with anyone
   └─ Works on phone
   └─ Live 24/7 while Replit tab is open

2. WORKING API ENDPOINT
   └─ POST /api/predict returns JSON
   └─ Use for integration

3. INTERACTIVE DASHBOARD
   └─ Professional UI
   └─ Live predictions
   └─ Charts and recommendations

4. PROOF OF CONCEPT
   └─ Shows judges: "System works!"
   └─ Perfect for demo video
   └─ Demonstrates AI predictions


════════════════════════════════════════════════════════════════════════════

⏱️ TIME BREAKDOWN
════════════════════════════════════════════════════════════════════════════

Step 1: Create Repl         1 minute
Step 2: Create requirements 1 minute
Step 3: Delete main.py      30 seconds
Step 4: Upload app.py       1 minute
Step 5: Upload model        2 minutes
Step 6: Open Shell          30 seconds
Step 7: Install packages    1 minute
Step 8: Run app.py          1 minute
Step 9: Get public URL      1 minute
Step 10: Test dashboard     2 minutes
Step 11: Share with team    1 minute
                           ─────────
TOTAL:                     12 minutes


════════════════════════════════════════════════════════════════════════════

✨ YOU'RE READY
════════════════════════════════════════════════════════════════════════════

Everything is prepared:
  ✓ app.py → Updated with correct host/port bindings
  ✓ xgboost_model.pkl → Trained and ready
  ✓ requirements.txt → All dependencies listed
  ✓ This guide → Crystal-clear steps

Next action:
  → Go to https://replit.com
  → Follow steps 1-11 above
  → 12 minutes later: LIVE BACKEND

Result:
  → Working API endpoint
  → Live dashboard
  → Ready for demo and submission

LET'S GO! 🚀


════════════════════════════════════════════════════════════════════════════

                    🎯 START HERE: https://replit.com

                Time: 12 minutes
                Result: Live API
                Status: Final step to complete system

════════════════════════════════════════════════════════════════════════════
