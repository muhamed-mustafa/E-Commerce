Product :
    - Name 
    - Description
    - Image
    - Category --> relation
    - Brand    --> relation
    - Variant  --> relation
    - Price 
    - Cost 
    - Created
    - Updated
    - New Product
    - Best Seller
    - Discount Price 
    - Slug 
    - Avaliable

ProductImage :
    - Product --> relation
    - Img

Category :
    - Name   --> Sub Category
    - Parent --> Main Category
    - Description
    - Image
    - Slug

ProductAlternative :
    - Product --> relation
    - Alternatives

ProductAccessory :
    - Product --> relation
    - Accessories

ProductBrand :
    - Name 
    - Description

ProductVariant :
    - Name 
    - Description

---------------------------------------------------------------------------------------------------------
Accounts :
    - Profile :
        - user --> relation
        - image
        - country
        - address
        - join_date
        - slug 