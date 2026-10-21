import pandas as pd
from Hour import Hour

class Asset:

    fixed_assets = pd.DataFrame(columns=['serial_no', 'name', 'asset_type', 'hour', 'cycle', 'days'])
    
    def __init__(self) -> None:
        """
        Initialize the variables
        """
        pass
    
    def create(self, **kwargs) -> pd.DataFrame:
        """
        Creates a new fixed asset
        """
        # Validate required fields
        required_fields = ['serial_no', 'name', 'asset_type', 'hour', 'cycle', 'days']
        for field in required_fields:
            if field not in kwargs:
                print(f"Error: Missing required field '{field}'")
                return 
        
        # Validate data types and formats
        if not isinstance(kwargs['serial_no'], str):
            print("Error: 'serial_no' should be a string")
            return
        
        if not isinstance(kwargs['name'], str):
            print("Error: 'name' should be a string")
            return
        
        if not isinstance(kwargs['asset_type'], str):
            if kwargs['asset_type'].capitalize() not in ['Aicraft', 'Assembly', 'Component']:
                print("Error: 'asset_type' should be a string")
            return
        
        if 'hour' in kwargs and not isinstance(kwargs['hour'], Hour):
            print("Error: 'hour' should be a string")
            return
        
        if 'cycle' in kwargs and not isinstance(kwargs['cycle'], int):
            print("Error: 'cycle' should be an integer")
            return
        
        if 'days' in kwargs and not isinstance(kwargs['days'], int):
            print("Error: 'days' should be an integer")
            return
        
        Asset.fixed_assets = pd.concat([Asset.fixed_assets, pd.DataFrame([kwargs])], ignore_index=True)
        Asset.read()
    
    def update(self, **kwargs):
        """
        Updates an existing fixed asset
        """
        try:
            if not isinstance(kwargs['serial_no'], str | int):
                print("Error: 'serial_no' should be a string / int")
                return
            if isinstance(kwargs['serial_no'], int):
                kwargs['serial_no'] = str(kwargs['serial_no'])
                print(kwargs['serial_no'])
        except KeyError:
            print("Error: 'serial_no' not defined")
            return
        
        if not Asset.fixed_assets.empty:
            if kwargs['serial_no']:
                asset_index = Asset.fixed_assets[Asset.fixed_assets['serial_no'] == kwargs['serial_no']].index[0]
                # print(asset_index)
                
                for _ in kwargs:
                
                    try:
                        Asset.fixed_assets.loc[asset_index, 'name'] = kwargs['name']
                        Asset.fixed_assets.loc[asset_index, 'asset_type'] = asset_type
                        Asset.fixed_assets.loc[asset_index, 'hour'] = Hour.from_string(hour)
                        Asset.fixed_assets.loc[asset_index, 'days'] = int(days)
                    except KeyError:
                        pass
                print("Asset updated successfully!")
                Asset.read()
                
            else:
                self.read()
                name = input("Enter the new name: ")
                asset_type = input("Enter the asset type: ")
                hour = input("Enter the hour:")
                days = input("Enter the days")
                Asset.fixed_assets.loc[asset_index, 'name'] = name
                Asset.fixed_assets.loc[asset_index, 'asset_type'] = asset_type
                Asset.fixed_assets.loc[asset_index, 'hour'] = Hour.from_string(hour)
                Asset.fixed_assets.loc[asset_index, 'days'] = int(days)

                print("Asset updated successfully!")
                Asset.read()
                
        else:
            print("Fixed assets is empty!")
    
    @classmethod
    def read(cls, **kwargs):
        """
        Reads the details of a fixed asset
        """
        
        print(cls.fixed_assets.to_markdown())

    def _delete(self, serial_no = None):
        """
        Deletes the record of a fixed asset
        """
        if not isinstance(serial_no, str | None):
            print("Error: 'serial_no' should be a string")
        
        if not Asset.fixed_assets.empty:
            
            if serial_no:
                try:
                    asset_index = Asset.fixed_assets[Asset.fixed_assets['serial_no'] == serial_no.upper()].index
                    Asset.fixed_assets.drop([asset_index[0]], inplace=True)
                    Asset.read()

                except IndexError:
                    print("Invalid input. Please enter a valid Serial no.")
            
            else:
                Asset.read()
                index_no = input("Enter the Index no of the asset to delete: ")
                try:
                    index_no = int(index_no)
                    if index_no in self.fixed_assets.index:
                        asset_serial_no = self.fixed_assets.loc[index_no, 'serial_no']
                        self.fixed_assets.drop(index_no, inplace=True)
                        print(f"Asset with serial no '{asset_serial_no}' has been deleted successfully!")
                    else:
                        print("Invalid index no.")
                except ValueError:
                    print("Invalid input. Please enter a valid index no.")
        else:
            print("No assets found.")


a = Asset()
a.create(
    serial_no='9N-DEMO',
    name='9N-DEMO',
    asset_type='Airplane',
    hour = Hour.from_string('120:00'),
    cycle = 250,
    days = 90
)

a.create(
    serial_no='101',
    name='101',
    asset_type='Assembly',
    hour = Hour(120,0),
    cycle = 250,
    days = 90
)

# a._delete()
# a.read()
a.update(
    serial_no = 101
)
# a._delete(serial_no='101')

# a.read()



