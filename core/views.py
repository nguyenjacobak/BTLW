# Add this function to your existing views.py file

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import sys

@csrf_exempt
def captcha_log(request):
    """
    Log CAPTCHA information to the server terminal
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expression = data.get('expression', 'Unknown')
            result = data.get('result', 'Unknown')
            
            # Print to terminal in a highly visible format
            captcha_message = f"""
╔════════════════════════════════════════════════════════════╗
║                     CAPTCHA GENERATED                      ║
╠════════════════════════════════════════════════════════════╣
║ Expression: {expression}
║ RESULT: {result}
╚════════════════════════════════════════════════════════════╝
"""
            print(captcha_message, file=sys.stderr)  # Print to stderr for better visibility in logs
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(f"Error logging CAPTCHA: {e}")
            return JsonResponse({'status': 'error'}, status=400)
    
    return JsonResponse({'status': 'invalid method'}, status=405)
