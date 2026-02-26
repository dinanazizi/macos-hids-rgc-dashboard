class RGCEngine:
    def __init__(self, governance_model):
        self.governance_model = governance_model
    
    def map_risk(self, activity):
        # Map activity to the governance rules
        risk_score = self.evaluate_risk(activity)
        if risk_score > self.governance_model['risk_threshold']:
            self.alert('High risk detected')
    
    def evaluate_risk(self, activity):
        # Basic rule-based risk evaluation
        return len(activity)  # Simplified risk evaluation for example
    
    def alert(self, message):
        print(f"ALERT: {message}")

# Example usage:
governance_model = {'risk_threshold': 10}
rgc_engine = RGCEngine(governance_model)
rgc_engine.map_risk("Unauthorized access to confidential data.")