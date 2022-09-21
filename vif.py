def compute_vif(considered_features):
    
    X_VIF = X_vif[considered_features]
    X_VIF['intercept'] = 1
    vif = pd.DataFrame()
    vif["Variable"] = X_VIF.columns
    vif["VIF"] = [variance_inflation_factor(X_VIF.values, i) for i in range(X_VIF.shape[1])]
    vif = vif[vif['Variable']!='intercept']
    return vif
  
  # considered_features = [...]
  # compute_vif(considered_features).sort_values('VIF', ascending=False)
