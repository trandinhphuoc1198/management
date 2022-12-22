class RedmineRouter:
    route_app_labels = {'redmine'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'redmine'
        return None
        
    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'redmine'
        return None
    
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'redmine'
        return None