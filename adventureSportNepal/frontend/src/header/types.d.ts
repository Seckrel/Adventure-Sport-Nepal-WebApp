export interface ItemsType {
    name: string;
    href: string;
    items?: null;
}

export interface NavigationItemType {
    name: string;
    items: null | ItemsType[];
}