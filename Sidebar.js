import React from 'react';
import SidebarNest from './SidebarNest';
import SidebarItem from './SidebarItem';

function Sidebar() {
  return (
    <div className="sidebar">
      {/* Add your Logo component here */}
      {/* Add other Sidebar components */}
      <SidebarNest />
      <SidebarItem />
    </div>
  );
}

export default Sidebar;
