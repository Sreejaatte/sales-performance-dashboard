class SalesService:
    def get_summary(self):
        return {
            "total_revenue": 1250000,
            "top_region": "South",
            "top_product": "Enterprise Plan",
            "growth_rate": 18.5
        }

sales_service = SalesService()
