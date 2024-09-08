ZONE_ID="zone_id"
API_TOKEN="api_token"
RECORD_ID="record_id"
DOMAIN="subdomain.example.com"

# Function to get the current public IP address
get_current_ip() {
  curl -s4 https://ifconfig.me
}

# Function to update Cloudflare DNS record
update_dns_record() {
  local current_ip=$1

  response=$(curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records/${RECORD_ID}" \
    -H "Authorization: Bearer ${API_TOKEN}" \
    -H "Content-Type: application/json" \
    --data "{\"type\":\"A\",\"name\":\"${DOMAIN}\",\"content\":\"${current_ip}\",\"ttl\":1,\"proxied\":false}")

  # Check if the update was successful
  if [[ "$response" == *"\"success\":true"* ]]; then
    echo "OK"
  else
    echo "Failed"
  fi
}

# Get the current public IP
current_ip=$(get_current_ip)

# Check if getting the current IP was successful
if [ $? -ne 0 ]; then
  echo "Failed"
  exit 1
fi

# Attempt to update DNS record
update_dns_record "${current_ip}"
